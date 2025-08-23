# ImageGeneration


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `background`                                                   | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | Background settings used in generation (OpenAI only)           |
| `created`                                                      | *OptionalNullable[int]*                                        | :heavy_minus_sign:                                             | The Unix timestamp (in seconds) of when the image was created. |
| `output_format`                                                | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | The output format of the generated image (OpenAI only)         |
| `quality`                                                      | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | The quality setting used for generation (OpenAI only)          |
| `size`                                                         | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | The size of the generated image (OpenAI only)                  |
| `usage`                                                        | [Optional[models.ImageUsage]](../models/imageusage.md)         | :heavy_minus_sign:                                             | N/A                                                            |
| `data`                                                         | List[[models.ImageData](../models/imagedata.md)]               | :heavy_check_mark:                                             | The list of generated images.                                  |