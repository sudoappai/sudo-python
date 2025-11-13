# ChatCompletionChunkUsage

Usage statistics for the completion request. When stream_options.include_usage is set, the final chunk before [DONE] will contain the full usage statistics, and all other chunks will include usage with a null value.


## Fields

| Field                       | Type                        | Required                    | Description                 |
| --------------------------- | --------------------------- | --------------------------- | --------------------------- |
| `completion_tokens`         | *int*                       | :heavy_check_mark:          | N/A                         |
| `completion_tokens_details` | *Optional[Any]*             | :heavy_minus_sign:          | N/A                         |
| `prompt_tokens`             | *int*                       | :heavy_check_mark:          | N/A                         |
| `prompt_tokens_details`     | *Optional[Any]*             | :heavy_minus_sign:          | N/A                         |
| `total_tokens`              | *int*                       | :heavy_check_mark:          | N/A                         |