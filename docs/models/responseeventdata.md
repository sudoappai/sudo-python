# ResponseEventData

Server-sent event from the streaming Responses API. Contains dynamic fields based on event type (response.created, response.output_text.delta, etc.)


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `type`                                                                                | *str*                                                                                 | :heavy_check_mark:                                                                    | The type of event (e.g., response.created, response.output_text.delta, response.done) |
| `sequence_number`                                                                     | *int*                                                                                 | :heavy_check_mark:                                                                    | Monotonically increasing sequence number for events in this response                  |
| `__pydantic_extra__`                                                                  | Dict[str, *Any*]                                                                      | :heavy_minus_sign:                                                                    | N/A                                                                                   |