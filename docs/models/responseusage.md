# ResponseUsage

Usage statistics for the API call


## Fields

| Field                             | Type                              | Required                          | Description                       |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `input_tokens`                    | *int*                             | :heavy_check_mark:                | Number of tokens in the input     |
| `input_tokens_details`            | *Optional[Any]*                   | :heavy_minus_sign:                | Breakdown of input token details  |
| `output_tokens`                   | *int*                             | :heavy_check_mark:                | Number of tokens in the output    |
| `output_tokens_details`           | *Optional[Any]*                   | :heavy_minus_sign:                | Breakdown of output token details |
| `total_tokens`                    | *int*                             | :heavy_check_mark:                | Total number of tokens used       |