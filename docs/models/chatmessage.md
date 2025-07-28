# ChatMessage


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `content`                                            | [models.MessageContent](../models/messagecontent.md) | :heavy_check_mark:                                   | N/A                                                  |
| `name`                                               | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | N/A                                                  |
| `role`                                               | *str*                                                | :heavy_check_mark:                                   | N/A                                                  |
| `tool_call_id`                                       | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | N/A                                                  |
| `tool_calls`                                         | List[[models.ToolCall](../models/toolcall.md)]       | :heavy_minus_sign:                                   | N/A                                                  |