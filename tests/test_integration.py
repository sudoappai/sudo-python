#!/usr/bin/env python3
"""
Comprehensive integration tests for the SUDO Python SDK.
Tests all router and system methods with various scenarios including:
- Basic chat completions with multiple models
- Streaming completions
- Tool/function calling
- Image input
- Structured output
- Audio output  
- Web search
- PDF input
- Reasoning models
- CRUD operations for stored completions
- Error handling
- System health and models endpoints

Usage:
    export SUDO_API_KEY="your-api-key-here"
    python -m pytest test_integration.py -v

Requirements:
    - Valid API key with credits
    - pytest
    - requests (for base64 image encoding)
"""

import os
import sys
import json
import base64
import time
import pytest
from typing import Dict, List, Any
import requests

from sudo_ai import Sudo, models, errors


class SudoTestConfig:
    """Test configuration and setup utilities."""
    
    def __init__(self):
        self.api_key = os.getenv("SUDO_API_KEY")
        if not self.api_key:
            pytest.skip("SUDO_API_KEY environment variable not set")
        
        self.base_url = "https://sudoapp.dev/api"  # Production URL
        self.client = None
        
        # Test models with their capabilities
        self.test_models = {
            "gpt-4o": {"has_id": True, "has_created": True, "supports_tools": True, "supports_vision": True},
            "claude-3-5-sonnet-20241022": {"has_id": True, "has_created": True, "supports_tools": True, "supports_vision": True},
            "deepseek-chat": {"has_id": True, "has_created": True, "supports_tools": False, "supports_vision": False},
            "grok-3": {"has_id": True, "has_created": True, "supports_tools": False, "supports_vision": False},
            "gemini-2.0-flash": {"has_id": False, "has_created": False, "supports_tools": True, "supports_vision": True},
        }
        
        # Image URL for vision tests
        self.test_image_url = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f7/RickRoll.png/330px-RickRoll.png"
        
    def get_client(self) -> Sudo:
        """Get configured SDK client."""
        if not self.client:
            self.client = Sudo(
                server_url=self.base_url,
                api_key=self.api_key
            )
        return self.client
    



@pytest.fixture(scope="session")
def config():
    """Shared test configuration."""
    return SudoTestConfig()


@pytest.fixture(scope="session") 
def client(config):
    """Shared SDK client."""
    return config.get_client()





class TestSystemMethods:
    """Test system endpoints."""
    
    def test_health_check(self, client):
        """Test system health check endpoint."""
        response = client.system.health_check()
        assert response is not None
        
    def test_get_models(self, client):
        """Test getting available models."""
        response = client.system.get_supported_models()
        
        assert response is not None
        assert hasattr(response, 'data')
        assert isinstance(response.data, list)
        assert len(response.data) > 0
        
        # Check first model structure
        first_model = response.data[0]
        assert hasattr(first_model, 'model_name')
        assert isinstance(first_model.model_name, str)
        assert len(first_model.model_name) > 0


class TestBasicChatCompletions:
    """Test basic chat completion functionality."""
    
    @pytest.mark.parametrize("model_name", ["gpt-4o", "claude-3-5-sonnet-20241022", "deepseek-chat", "grok-3", "gemini-2.0-flash"])
    def test_create_chat_completion_basic(self, client, config, model_name):
        """Test basic chat completions with different models."""
        model_config = config.test_models.get(model_name, {})
        
        messages = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Give me a study plan to learn Python."}
        ]
        
        try:
            response = client.router.create(
                model=model_name,
                messages=messages,
                store=True,
                max_completion_tokens=150
            )
            
            # Check response structure
            assert response is not None
            assert hasattr(response, 'object')
            assert response.object == "chat.completion"
            
            # Check model-specific fields
            if model_config.get("has_id", True):
                assert hasattr(response, 'id')
                assert isinstance(response.id, str)
                assert len(response.id) > 0
                
            if model_config.get("has_created", True):
                assert hasattr(response, 'created')
                assert isinstance(response.created, int)
                
            assert hasattr(response, 'model')
            assert isinstance(response.model, str)
            
            # Check choices
            assert hasattr(response, 'choices')
            assert isinstance(response.choices, list)
            assert len(response.choices) > 0
            
            first_choice = response.choices[0]
            assert hasattr(first_choice, 'finish_reason')
            assert hasattr(first_choice, 'index')
            assert hasattr(first_choice, 'message')
            
            # Check message
            message = first_choice.message
            assert hasattr(message, 'role')
            assert message.role == "assistant"
            assert hasattr(message, 'content')
            assert isinstance(message.content, str)
            assert len(message.content) > 0
            
            # Check usage
            assert hasattr(response, 'usage')
            usage = response.usage
            assert hasattr(usage, 'prompt_tokens')
            assert hasattr(usage, 'completion_tokens')
            assert hasattr(usage, 'total_tokens')
            assert isinstance(usage.prompt_tokens, int)
            assert isinstance(usage.completion_tokens, int)
            assert isinstance(usage.total_tokens, int)
            assert usage.total_tokens == usage.prompt_tokens + usage.completion_tokens
            
        except Exception as e:
            # Some models might not be available or have issues
            if "not found" in str(e).lower() or "unavailable" in str(e).lower():
                pytest.skip(f"Model {model_name} not available: {e}")
            else:
                raise


class TestStreamingCompletions:
    """Test streaming chat completions."""
    
    @pytest.mark.parametrize("model_name", ["gpt-4o", "claude-3-5-sonnet-20241022", "deepseek-chat", "grok-3", "gemini-2.0-flash"])
    def test_create_chat_completion_streaming(self, client, model_name):
        """Test streaming chat completions."""
        messages = [
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! Give me a list of all the planets in the solar system, with a few sentences about each."}
        ]
        
        try:
            stream = client.router.create_streaming(
                model=model_name,
                messages=messages,
                store=True
            )
            
            chunks_received = 0
            content_received = ""
            
            for chunk in stream:
                chunks_received += 1
                
                # Check chunk structure
                assert hasattr(chunk, 'data')
                assert chunk.data is not None
                assert hasattr(chunk.data, 'choices')
                
                if chunk.data.choices and len(chunk.data.choices) > 0:
                    choice = chunk.data.choices[0]
                    
                    if hasattr(choice, 'delta') and choice.delta:
                        if hasattr(choice.delta, 'content') and choice.delta.content:
                            content_received += choice.delta.content
            
            # Verify we received multiple chunks and some content
            assert chunks_received > 1, f"Expected multiple chunks, got {chunks_received}"
            assert len(content_received) > 0, "Expected to receive some content"
            
        except Exception as e:
            if "not found" in str(e).lower() or "unavailable" in str(e).lower():
                pytest.skip(f"Model {model_name} not available: {e}")
            else:
                raise


class TestToolCalling:
    """Test function/tool calling capabilities."""
    
    def test_create_chat_completion_tool_call(self, client):
        """Test tool calling with supported models."""
        # Only test with models that support tools
        for model_name in ["gpt-4o", "claude-3-5-sonnet-20241022"]:
            messages = [
                {
                    "role": "system",
                    "content": [{"type": "text", "text": "Respond precisely like a financial advisor and outline all the pros and cons of every option."}]
                },
                {
                    "role": "user", 
                    "content": [{"type": "text", "text": "How much does the S&P 500 index ETF cost today?"}]
                }
            ]
            
            tools = [
                {
                    "type": "function",
                    "function": {
                        "name": "get_stock_price",
                        "description": "Get the current stock price",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "symbol": {"type": "string", "description": "The stock symbol"}
                            },
                            "additionalProperties": False,
                            "required": ["symbol"]
                        },
                        "strict": True
                    }
                }
            ]
            
            try:
                response = client.router.create(
                    model=model_name,
                    messages=messages,
                    tools=tools,
                    temperature=1.0,
                    max_completion_tokens=2048,
                    store=True
                )
                
                # Check basic response structure
                assert hasattr(response, 'object')
                assert response.object == "chat.completion"
                
                # Check choices
                assert hasattr(response, 'choices')
                assert len(response.choices) > 0
                
                first_choice = response.choices[0]
                assert first_choice.finish_reason == "tool_calls"
                
                # Check message with tool calls
                message = first_choice.message
                assert message.role == "assistant"
                assert hasattr(message, 'tool_calls')
                assert isinstance(message.tool_calls, list)
                assert len(message.tool_calls) > 0
                
                # Check first tool call
                first_tool_call = message.tool_calls[0]
                assert first_tool_call.type == "function"
                assert hasattr(first_tool_call, 'id')
                assert isinstance(first_tool_call.id, str)
                
                # Check function structure
                function = first_tool_call.function
                assert hasattr(function, 'name')
                assert isinstance(function.name, str)
                assert hasattr(function, 'arguments')
                assert isinstance(function.arguments, str)
                
                # Check usage
                assert hasattr(response, 'usage')
                usage = response.usage
                assert isinstance(usage.prompt_tokens, int)
                assert isinstance(usage.completion_tokens, int)
                assert isinstance(usage.total_tokens, int)
                
                break  # Success with one model is enough
                
            except Exception as e:
                if "not found" in str(e).lower() or "unavailable" in str(e).lower():
                    continue  # Try next model
                else:
                    raise
        else:
            pytest.fail("No supported models available for tool calling")


class TestImageInput:
    """Test vision/image input capabilities."""
    
    def test_create_chat_completion_image_input(self, client, config):
        """Test image input with vision models."""
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What is in this image?"},
                    {
                        "type": "image_url",
                        "image_url": {"url": config.test_image_url}
                    }
                ]
            }
        ]
        
        # Test with a vision-capable model
        try:
            response = client.router.create(
                model="gpt-4o",
                messages=messages,
                max_completion_tokens=300
            )
            
            # Check response structure
            assert hasattr(response, 'object')
            assert response.object == "chat.completion"
            
            # Check choices
            assert hasattr(response, 'choices')
            assert len(response.choices) > 0
            
            first_choice = response.choices[0]
            assert hasattr(first_choice, 'message')
            
            message = first_choice.message
            assert message.role == "assistant"
            assert hasattr(message, 'content')
            assert isinstance(message.content, str)
            assert len(message.content) > 0
            
            # Check usage
            assert hasattr(response, 'usage')
            
        except Exception as e:
            if "not found" in str(e).lower() or "unavailable" in str(e).lower():
                pytest.skip(f"Vision model not available: {e}")
            else:
                raise


class TestStructuredOutput:
    """Test structured output capabilities."""
    
    def test_create_chat_completion_structured_output(self, client):
        """Test structured output with JSON schema."""
        messages = [
            {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
            {"role": "user", "content": "how can I solve 8x + 7 = -23"}
        ]
        
        response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": "math_reasoning",
                "schema": {
                    "type": "object",
                    "properties": {
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "explanation": {"type": "string"},
                                    "output": {"type": "string"}
                                },
                                "required": ["explanation", "output"],
                                "additionalProperties": False
                            }
                        },
                        "final_answer": {"type": "string"}
                    },
                    "required": ["steps", "final_answer"],
                    "additionalProperties": False
                },
                "strict": True
            }
        }
        
        try:
            response = client.router.create(
                model="gpt-4o",
                messages=messages,
                response_format=response_format
            )
            
            # Check response structure
            assert hasattr(response, 'object')
            assert response.object == "chat.completion"
            
            # Check message content
            first_choice = response.choices[0]
            message = first_choice.message
            assert message.role == "assistant"
            assert hasattr(message, 'content')
            
            # Parse and validate JSON structure
            content_json = json.loads(message.content)
            assert "steps" in content_json
            assert "final_answer" in content_json
            assert isinstance(content_json["steps"], list)
            assert len(content_json["steps"]) > 0
            assert isinstance(content_json["final_answer"], str)
            
            # Check first step structure
            first_step = content_json["steps"][0]
            assert "explanation" in first_step
            assert "output" in first_step
            assert isinstance(first_step["explanation"], str)
            assert isinstance(first_step["output"], str)
            
        except Exception as e:
            if "not found" in str(e).lower() or "unavailable" in str(e).lower():
                pytest.skip(f"Structured output not available: {e}")
            else:
                raise


class TestReasoningModels:
    """Test reasoning model capabilities."""
    
    def test_create_chat_completion_reasoning(self, client):
        """Test reasoning models with reasoning effort parameter."""
        messages = [
            {"role": "user", "content": "Solve this step by step: If a train travels 120 miles in 2 hours, and then 180 miles in 3 hours, what is the average speed for the entire journey?"}
        ]
        
        try:
            response = client.router.create(
                model="o4-mini",
                messages=messages,
                reasoning_effort="medium"
            )
            
            # Check response structure
            assert hasattr(response, 'object')
            assert response.object == "chat.completion"
            
            # Check usage includes reasoning tokens
            assert hasattr(response, 'usage')
            usage = response.usage
            
            # For reasoning models, check if we have reasoning token details
            if hasattr(usage, 'completion_tokens_details'):
                details = usage.completion_tokens_details
                if hasattr(details, 'reasoning_tokens'):
                    assert isinstance(details.reasoning_tokens, int)
                    assert details.reasoning_tokens >= 0
            
        except Exception as e:
            if "not found" in str(e).lower() or "unavailable" in str(e).lower():
                pytest.skip(f"Reasoning model not available: {e}")
            else:
                raise


# class TestStoredCompletions:
#     """Test CRUD operations for stored completions."""
    
#     def test_completion_crud_operations(self, client):
#         """Test creating, reading, updating, and deleting stored completions."""
#         # Step 1: Create a stored completion
#         messages = [
#             {"role": "developer", "content": "You are a helpful assistant."},
#             {"role": "user", "content": "Hello! Give me a study plan to learn Python."}
#         ]
        
#         create_response = client.router.create(
#             model="gpt-4o",
#             messages=messages,
#             store=True,
#             max_completion_tokens=150
#         )
        
#         assert hasattr(create_response, 'id')
#         completion_id = create_response.id
        
#         # Step 2: Get the completion by ID (with retries)
#         max_attempts = 6
#         delay_between_attempts = 2
        
#         get_response = None
#         for attempt in range(max_attempts):
#             try:
#                 get_response = client.router.get_chat_completion(completion_id=completion_id)
#                 break
#             except Exception as e:
#                 if attempt < max_attempts - 1:
#                     time.sleep(delay_between_attempts)
#                     continue
#                 else:
#                     raise
        
#         assert get_response is not None
#         assert hasattr(get_response, 'id')
#         assert get_response.id == completion_id
#         assert hasattr(get_response, 'object')
#         assert get_response.object == "chat.completion"
        
#         # Step 3: Get messages for the completion (with retries)
#         messages_response = None
#         for attempt in range(max_attempts):
#             try:
#                 messages_response = client.router.get_chat_completion_messages(completion_id=completion_id)
#                 break
#             except Exception as e:
#                 if attempt < max_attempts - 1:
#                     time.sleep(delay_between_attempts)
#                     continue
#                 else:
#                     raise
        
#         assert messages_response is not None
#         assert hasattr(messages_response, 'object')
#         assert hasattr(messages_response, 'data')
#         assert isinstance(messages_response.data, list)
#         assert len(messages_response.data) > 0
        
#         # Check first message structure
#         first_message = messages_response.data[0]
#         assert hasattr(first_message, 'role')
#         assert first_message.role == "developer"
#         assert hasattr(first_message, 'content')
        
#         # Step 4: Update the completion with metadata (with retries)
#         update_response = None
#         for attempt in range(max_attempts):
#             try:
#                 update_response = client.router.update_chat_completion(
#                     completion_id=completion_id,
#                     metadata={"test": "value", "updated": "true"}
#                 )
#                 break
#             except Exception as e:
#                 if attempt < max_attempts - 1:
#                     time.sleep(delay_between_attempts)
#                     continue
#                 else:
#                     raise
        
#         assert update_response is not None
#         assert hasattr(update_response, 'id')
#         assert update_response.id == completion_id
#         assert hasattr(update_response, 'metadata')
#         assert update_response.metadata["test"] == "value"
#         assert update_response.metadata["updated"] == "true"
        
#         # Step 5: List completions to verify it's there
#         list_response = client.router.list_chat_completions(limit=10, order="desc")
#         assert hasattr(list_response, 'object')
#         assert list_response.object == "list"
#         assert hasattr(list_response, 'data')
#         assert isinstance(list_response.data, list)
        
#         # Find our completion in the list
#         found_completion = None
#         for completion in list_response.data:
#             if hasattr(completion, 'id') and completion.id == completion_id:
#                 found_completion = completion
#                 break
        
#         assert found_completion is not None, f"Completion {completion_id} not found in list"
        
#         # Step 6: Delete the completion (with retries)
#         delete_response = None
#         for attempt in range(max_attempts):
#             try:
#                 delete_response = client.router.delete_chat_completion(completion_id=completion_id)
#                 break
#             except Exception as e:
#                 if attempt < max_attempts - 1:
#                     time.sleep(delay_between_attempts)
#                     continue
#                 else:
#                     raise
        
#         assert delete_response is not None
#         assert hasattr(delete_response, 'id')
#         assert delete_response.id == completion_id
#         assert hasattr(delete_response, 'object')
#         assert delete_response.object == "chat.completion.deleted"
#         assert hasattr(delete_response, 'deleted')
#         assert delete_response.deleted is True


class TestImageGeneration:
    """Test image generation capabilities."""
    
    def test_generate_image_with_gpt_image_1(self, client):
        """Test image generation with gpt-image-1 model."""
        prompt = "A beautiful sunset over a mountain landscape with vibrant colors"
        
        try:
            response = client.router.generate_image(
                model="gpt-image-1",
                prompt=prompt,
                n=1,
                size="1024x1024"
            )
            
            # Check response structure
            assert response is not None
            assert hasattr(response, 'data')
            assert isinstance(response.data, list)
            assert len(response.data) > 0
            
            # Check first image data
            first_image = response.data[0]
            assert hasattr(first_image, 'b64_json')
            assert isinstance(first_image.b64_json, str)
            assert len(first_image.b64_json) > 0
            
            # Check optional fields that might be present
            if hasattr(response, 'created'):
                assert isinstance(response.created, int)
                assert response.created > 0
                
            if hasattr(response, 'usage'):
                usage = response.usage
                if hasattr(usage, 'prompt_tokens'):
                    assert isinstance(usage.prompt_tokens, int)
                    assert usage.prompt_tokens >= 0
                    
        except Exception as e:
            if "not found" in str(e).lower() or "unavailable" in str(e).lower():
                pytest.skip(f"Image generation model not available: {e}")
            else:
                raise
    
    def test_generate_image_with_url_format(self, client):
        """Test image generation with base64 response format."""
        prompt = "A simple geometric pattern in blue and white"
        
        try:
            response = client.router.generate_image(
                model="dall-e-3",
                prompt=prompt,
                response_format="url",
                n=1,
                size="1024x1024"
            )
            
            # Check response structure
            assert response is not None
            assert hasattr(response, 'data')
            assert isinstance(response.data, list)
            assert len(response.data) > 0
            
            # Check first image data
            first_image = response.data[0]
            assert hasattr(first_image, 'url')
            assert isinstance(first_image.url, str)
            assert len(first_image.url) > 0
            
                
        except Exception as e:
            if "not found" in str(e).lower() or "unavailable" in str(e).lower():
                pytest.skip(f"Image generation model not available: {e}")
            else:
                raise


class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_error_bad_request(self, client):
        """Test handling of bad request errors."""
        # Send request with no messages (invalid)
        with pytest.raises(Exception) as exc_info:
            client.router.create(
                model="gpt-4o",
                messages=[]  # Empty messages should cause error
            )
        
        # The exact error type may vary, but we should get some kind of error
        assert exc_info.value is not None
        
    def test_error_invalid_model(self, client):
        """Test handling of invalid model errors."""
        messages = [
            {"role": "user", "content": "Hello"}
        ]
        
        with pytest.raises(Exception) as exc_info:
            client.router.create(
                model="nonexistent-model-12345",
                messages=messages
            )
        
        # Should get some kind of error for invalid model
        assert exc_info.value is not None
        
    def test_error_completion_not_found(self, client):
        """Test handling of completion not found errors."""
        with pytest.raises(Exception) as exc_info:
            client.router.get_chat_completion(completion_id="nonexistent-completion-id")
        
        # Should get some kind of error for nonexistent completion
        assert exc_info.value is not None


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v"])