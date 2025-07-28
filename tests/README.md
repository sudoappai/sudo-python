# SUDO Python SDK Integration Tests

This directory contains comprehensive integration tests for the SUDO Python SDK that validate all functionality including:

## Test Coverage

### Router Methods (7 AI Routing Methods)
- **Basic Chat Completions** - Tests with multiple models (GPT-4o, Claude, DeepSeek, Grok, Gemini)
- **Streaming Completions** - Tests real-time streaming responses
- **Tool/Function Calling** - Tests function calling capabilities
- **Image Input** - Tests vision model capabilities with image URLs
- **Structured Output** - Tests JSON schema-based structured responses
- **Reasoning Models** - Tests reasoning capabilities and reasoning tokens
- **Stored Completion CRUD** - Tests create, read, update, delete operations for stored completions

### System Methods (2 System Methods)
- **Health Check** - Tests API health status
- **Models** - Tests retrieving available models

### Error Handling
- **Bad Request Errors** - Tests validation error handling
- **Invalid Model Errors** - Tests error handling for unsupported models
- **Not Found Errors** - Tests handling of missing resources

## Requirements

- Python 3.7+
- Valid SUDO API key with credits
- Internet connection

## Quick Start

### Option 1: Use the Test Runner (Recommended)

```bash
# Set your API key
export SUDO_API_KEY="your-api-key-here"

# Run all tests
cd sdk/sudo-python/tests
python run_tests.py
```

### Option 2: Use pytest directly

```bash
# Set your API key
export SUDO_API_KEY="your-api-key-here"

# Create and activate virtual environment
cd sdk/sudo-python/tests
python3 -m venv venv
source venv/bin/activate

# Install the SUDO SDK in development mode
cd .. && pip install -e .

# Install test dependencies
cd tests && pip install -r requirements-test.txt

# Run all tests
python -m pytest test_integration.py -v

# Run specific test classes
python -m pytest test_integration.py::TestBasicChatCompletions -v
python -m pytest test_integration.py::TestStreamingCompletions -v
python -m pytest test_integration.py::TestToolCalling -v
```

## Test Organization

The tests are organized into logical classes:

- `TestSystemMethods` - System health and model endpoints
- `TestBasicChatCompletions` - Basic completion functionality across models
- `TestStreamingCompletions` - Streaming completion functionality
- `TestToolCalling` - Function/tool calling capabilities
- `TestImageInput` - Vision/image input testing
- `TestStructuredOutput` - JSON schema-based structured outputs
- `TestReasoningModels` - Reasoning model capabilities
- `TestStoredCompletions` - Full CRUD operations for stored completions
- `TestErrorHandling` - Error scenarios and edge cases

## Models Tested

The tests include these models with their specific capabilities:

| Model | ID/Created Fields | Tool Calling | Vision | Notes |
|-------|------------------|--------------|--------|-------|
| gpt-4o | ✅ | ✅ | ✅ | Full feature support |
| claude-3-5-sonnet-20241022 | ✅ | ✅ | ✅ | Full feature support |
| deepseek-chat | ✅ | ❌ | ❌ | Basic completion only |
| grok-3 | ✅ | ❌ | ❌ | Basic completion only |
| gemini-2.0-flash | ❌ | ✅ | ✅ | No ID/created fields |

## Test Scenarios Covered

### 1. Basic Completions
- Tests all supported models
- Validates response structure (id, created, model, choices, usage)
- Checks message content and role
- Validates token usage statistics

### 2. Streaming Completions
- Tests real-time streaming with multiple models
- Validates chunk structure and delta content
- Ensures multiple chunks are received
- Verifies content accumulation

### 3. Tool/Function Calling
- Tests with realistic financial advisor scenario
- Validates tool call structure and function parameters
- Checks finish_reason is "tool_calls"
- Tests with strict parameter validation

### 4. Vision/Image Input
- Tests image understanding with public image URL
- Validates multimodal message structure
- Ensures proper image processing and description

### 5. Structured Output
- Tests with complex JSON schema (math problem solving)
- Validates strict schema adherence
- Checks nested object and array structures
- Ensures required fields are present

### 6. Reasoning Models
- Tests reasoning effort parameters
- Validates reasoning token usage tracking
- Checks reasoning token details in usage statistics

### 7. Stored Completions CRUD
- **Create**: Creates completion with store=true
- **Read**: Retrieves completion by ID with retry logic
- **Update**: Updates completion metadata
- **Delete**: Removes stored completion
- **List**: Validates completion appears in listings
- **Messages**: Retrieves completion message history

### 8. Error Handling
- Tests malformed requests (empty messages)
- Tests invalid model names
- Tests accessing non-existent completions
- Validates proper error responses

## Configuration

The tests use these default settings:

- **Server URL**: `https://sudoapp.dev/api` (production)
- **Retry Logic**: 6 attempts with 2-second delays for async operations
- **Timeouts**: Standard SDK timeouts
- **Test Image**: Public Wikipedia image for vision tests

You can customize these by modifying the `SudoTestConfig` class in `test_integration.py`.

## Running Specific Tests

```bash
# Test only system methods
python -m pytest test_integration.py::TestSystemMethods -v

# Test only streaming
python -m pytest test_integration.py::TestStreamingCompletions -v

# Test specific model
python -m pytest test_integration.py::TestBasicChatCompletions::test_create_chat_completion_basic[gpt-4o] -v

# Test CRUD operations
python -m pytest test_integration.py::TestStoredCompletions::test_completion_crud_operations -v
```

## Troubleshooting

### Common Issues

1. **API Key Issues**
   ```
   SUDO_API_KEY environment variable not set
   ```
   **Solution**: Set your API key: `export SUDO_API_KEY="your-key-here"`

2. **Import Errors / Module Not Found**
   ```
   ModuleNotFoundError: No module named 'sudo'
   ModuleNotFoundError: No module named 'typing_extensions'
   ```
   **Solution**: Make sure you've installed the SUDO SDK in development mode: `pip install -e .` from the `sdk/sudo-python/` directory

3. **Model Not Available**
   ```
   Model xyz not available
   ```
   **Solution**: Tests will skip unavailable models automatically

3. **Rate Limiting**
   ```
   Too many requests
   ```
   **Solution**: Tests include retry logic; wait and retry

4. **Network Issues**
   ```
   Connection timeout
   ```
   **Solution**: Check internet connection and API status

### Test Failures

If tests fail:

1. Check API key validity and credits
2. Verify internet connection
3. Check API status at SUDO's status page
4. Run individual test classes to isolate issues
5. Review error messages for specific model issues

## Performance

- **Full test suite**: ~5-10 minutes depending on API response times
- **Individual test classes**: ~30 seconds to 2 minutes
- **Network dependent**: Streaming and image tests require stable connection

## Contributing

When adding new tests:

1. Follow the existing class structure
2. Add proper docstrings and assertions
3. Include error handling for model availability
4. Use parametrized tests for multiple models where applicable
5. Update this README with new test coverage 