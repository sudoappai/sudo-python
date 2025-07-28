# ChatCompletion


## Fields

| Field                                                  | Type                                                   | Required                                               | Description                                            |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------ |
| `choices`                                              | List[[models.Choice](../models/choice.md)]             | :heavy_check_mark:                                     | N/A                                                    |
| `created`                                              | *int*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `id`                                                   | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `model`                                                | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `object`                                               | *str*                                                  | :heavy_check_mark:                                     | N/A                                                    |
| `service_tier`                                         | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `system_fingerprint`                                   | *OptionalNullable[str]*                                | :heavy_minus_sign:                                     | N/A                                                    |
| `usage`                                                | [models.Usage](../models/usage.md)                     | :heavy_check_mark:                                     | N/A                                                    |
| `metadata`                                             | Dict[str, *str*]                                       | :heavy_minus_sign:                                     | Developer-defined metadata attached to the completion. |