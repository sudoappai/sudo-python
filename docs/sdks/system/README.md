# System
(*system*)

## Overview

### Available Operations

* [health_check](#health_check) - Check if the Sudo API and backend infrastructure are health and ready to accept connections.
* [get_supported_models](#get_supported_models) - Get a list of all AI models supported in the Sudo API.

## health_check

Check if the Sudo API and backend infrastructure are health and ready to accept connections.

### Example Usage

```python
import os
from sudo import Sudo


with Sudo(
    server_url="https://api.example.com",
    api_key=os.getenv("SUDO_API_KEY", ""),
) as s_client:

    res = s_client.system.health_check()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[Any](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_supported_models

Get a list of all AI models supported in the Sudo API.

### Example Usage

```python
import os
from sudo import Sudo


with Sudo(
    server_url="https://api.example.com",
    api_key=os.getenv("SUDO_API_KEY", ""),
) as s_client:

    res = s_client.system.get_supported_models()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.SupportedModelsList](../../models/supportedmodelslist.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| errors.ErrorResponse | 401                  | application/json     |
| errors.ErrorResponse | 500                  | application/json     |
| errors.APIError      | 4XX, 5XX             | \*/\*                |