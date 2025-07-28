# ChatCompletionRequestJSONResponseFormatUnion

An object specifying the format that the model must output. Compatible with GPT-4o, GPT-4o mini, GPT-4 Turbo and all GPT-3.5 Turbo models newer than gpt-3.5-turbo-1106. Setting to { "type": "json_schema", "json_schema": {...} } enables Structured Outputs which guarantee the model will match your supplied JSON schema. Setting to { "type": "json_object" } enables JSON mode, which guarantees the message the model generates is valid JSON.


## Supported Types

### `models.ChatCompletionRequestJSONResponseFormatText`

```python
value: models.ChatCompletionRequestJSONResponseFormatText = /* values here */
```

### `models.ChatCompletionRequestJSONResponseFormatJSONObject`

```python
value: models.ChatCompletionRequestJSONResponseFormatJSONObject = /* values here */
```

### `models.ChatCompletionRequestJSONResponseFormatJSONSchema`

```python
value: models.ChatCompletionRequestJSONResponseFormatJSONSchema = /* values here */
```

