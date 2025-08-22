# ImageUsage


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `input_tokens`                                               | *int*                                                        | :heavy_check_mark:                                           | Number of tokens in the input prompt.                        |
| `input_tokens_details`                                       | [models.ImageInputTokens](../models/imageinputtokens.md)     | :heavy_check_mark:                                           | N/A                                                          |
| `output_tokens`                                              | *int*                                                        | :heavy_check_mark:                                           | Number of tokens used for the generated image.               |
| `total_tokens`                                               | *int*                                                        | :heavy_check_mark:                                           | Total number of tokens used in the request (input + output). |