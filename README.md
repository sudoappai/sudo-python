# sudo

Developer-friendly & type-safe Python SDK specifically catered to leverage *sudo* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=sudo&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


<!-- <br /><br />
> [!IMPORTANT]
> This SDK is not yet ready for production use. To complete setup please follow the steps outlined in your [workspace](https://app.speakeasy.com/org/sudo/sudo). Delete this section before > publishing to a package manager. -->

<!-- Start Summary [summary] -->
## Summary


<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
- [sudo](#sudo)
  - [Summary](#summary)
  - [Table of Contents](#table-of-contents)
  - [SDK Installation](#sdk-installation)
    - [uv](#uv)
    - [PIP](#pip)
    - [Poetry](#poetry)
    - [Shell and script usage with `uv`](#shell-and-script-usage-with-uv)
  - [IDE Support](#ide-support)
    - [PyCharm](#pycharm)
  - [SDK Example Usage](#sdk-example-usage)
    - [Example](#example)
  - [Authentication](#authentication)
    - [Per-Client Security Schemes](#per-client-security-schemes)
  - [Available Resources and Operations](#available-resources-and-operations)
    - [router](#router)
    - [system](#system)
  - [Server-sent event streaming](#server-sent-event-streaming)
  - [Retries](#retries)
  - [Error Handling](#error-handling)
    - [Example](#example-1)
    - [Error Classes](#error-classes)
  - [Custom HTTP Client](#custom-http-client)
  - [Resource Management](#resource-management)
  - [Debugging](#debugging)
- [Development](#development)
  - [Maturity](#maturity)
  - [Contributions](#contributions)
    - [SDK Created by Speakeasy](#sdk-created-by-speakeasy)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

<!-- > [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide). -->


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add sudo-ai
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install sudo-ai
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add sudo-ai
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from sudo-ai python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "sudo-ai",
# ]
# ///

from sudo_ai import Sudo

sdk = Sudo(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
import os
from sudo_ai import Sudo


with Sudo(
    server_url="https://api.example.com",
    api_key=os.getenv("SUDO_API_KEY", ""),
) as sudo:

    res = sudo.system.health_check()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from sudo_ai import Sudo

async def main():

    async with Sudo(
        server_url="https://api.example.com",
        api_key=os.getenv("SUDO_API_KEY", ""),
    ) as sudo:

        res = await sudo.system.health_check_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type | Scheme      | Environment Variable |
| --------- | ---- | ----------- | -------------------- |
| `api_key` | http | HTTP Bearer | `SUDO_API_KEY`       |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
```python
import os
from sudo_ai import Sudo


with Sudo(
    server_url="https://api.example.com",
    api_key=os.getenv("SUDO_API_KEY", ""),
) as sudo:

    res = sudo.system.health_check()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [router](docs/sdks/router/README.md)

* [list_chat_completions](docs/sdks/router/README.md#list_chat_completions) - *[OpenAI Only]* Get a list of saved Chat Completions. Only Chat Completions that have been stored with the `store` parameter set to true will be returned.
* [create](docs/sdks/router/README.md#create) - Create a model response for the given string of prompts.
* [create_streaming](docs/sdks/router/README.md#create_streaming) - Create a streaming model response for the given string of prompts using server-sent events.
* [get_chat_completion](docs/sdks/router/README.md#get_chat_completion) - *[OpenAI Only]* Get a Chat Completion. Only Chat Completions that have been stored with the `store` parameter set to true will be returned.
* [update_chat_completion](docs/sdks/router/README.md#update_chat_completion) - *[OpenAI Only]* Update a Chat Completion with some metadata. Only Chat Completions that have been stored with the `store` parameter set to true will be returned.
* [delete_chat_completion](docs/sdks/router/README.md#delete_chat_completion) - *[OpenAI Only]* Delete a stored Chat Completion. Only Chat Completions that have been stored with the `store` parameter set to true will be returned.
* [get_chat_completion_messages](docs/sdks/router/README.md#get_chat_completion_messages) - *[OpenAI Only]* Get the array of messages for a saved Chat Completion. Only Chat Completions that have been stored with the `store` parameter set to true will be returned.
* [generate_image](docs/sdks/router/README.md#generate_image) - Generate Image


### [system](docs/sdks/system/README.md)

* [health_check](docs/sdks/system/README.md#health_check) - Check if the Sudo API and backend infrastructure are health and ready to accept connections.
* [get_supported_models](docs/sdks/system/README.md#get_supported_models) - Get a list of all AI models supported in the Sudo API.

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Server-sent event streaming [eventstream] -->
## Server-sent event streaming

[Server-sent events][mdn-sse] are used to stream content from certain
operations. These operations will expose the stream as [Generator][generator] that
can be consumed using a simple `for` loop. The loop will
terminate when the server no longer has any events to send and closes the
underlying connection.  

The stream is also a [Context Manager][context-manager] and can be used with the `with` statement and will close the
underlying connection when the context is exited.

```python
import os
from sudo_ai import Sudo


with Sudo(
    server_url="https://api.example.com",
    api_key=os.getenv("SUDO_API_KEY", ""),
) as sudo:

    res = sudo.router.create_streaming(messages=[
        {
            "content": "You are a helpful assistant.",
            "role": "developer",
        },
        {
            "content": "Hello! How are you?",
            "role": "user",
        },
    ], model="gpt-4o")

    with res as event_stream:
        for chunk in event_stream:
            # Access the chunk data
            if chunk.data and chunk.data.choices:
                for choice in chunk.data.choices:
                    if choice.delta and choice.delta.content:
                        print(choice.delta.content, end="", flush=True)

```

[mdn-sse]: https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events
[generator]: https://book.pythontips.com/en/latest/generators.html
[context-manager]: https://book.pythontips.com/en/latest/context_managers.html
<!-- End Server-sent event streaming [eventstream] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
import os
from sudo_ai import Sudo
from sudo_ai.utils import BackoffStrategy, RetryConfig


with Sudo(
    server_url="https://api.example.com",
    api_key=os.getenv("SUDO_API_KEY", ""),
) as sudo:

    res = sudo.system.health_check(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
import os
from sudo_ai import Sudo
from sudo_ai.utils import BackoffStrategy, RetryConfig


with Sudo(
    server_url="https://api.example.com",
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    api_key=os.getenv("SUDO_API_KEY", ""),
) as sudo:

    res = sudo.system.health_check()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`SudoError`](./src/sudo_ai/errors/sudoerror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
import os
from sudo_ai import Sudo, errors


with Sudo(
    server_url="https://api.example.com",
    api_key=os.getenv("SUDO_API_KEY", ""),
) as sudo:
    res = None
    try:

        res = sudo.system.get_supported_models()

        # Handle response
        print(res)


    except errors.SudoError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.ErrorResponse):
            print(e.data.error)  # models.ErrorDetail
```

### Error Classes
**Primary errors:**
* [`SudoError`](./src/sudo_ai/errors/sudoerror.py): The base class for HTTP error responses.
  * [`ErrorResponse`](./src/sudo_ai/errors/errorresponse.py): *

<details><summary>Less common errors (5)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`SudoError`](./src/sudo_ai/errors/sudoerror.py)**:
* [`ResponseValidationError`](./src/sudo_ai/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from sudo_ai import Sudo
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Sudo(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from sudo_ai import Sudo
from sudo_ai.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Sudo(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Sudo` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
import os
from sudo_ai import Sudo
def main():

    with Sudo(
        server_url="https://api.example.com",
        api_key=os.getenv("SUDO_API_KEY", ""),
    ) as sudo:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Sudo(
        server_url="https://api.example.com",
        api_key=os.getenv("SUDO_API_KEY", ""),
    ) as sudo:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from sudo_ai import Sudo
import logging

logging.basicConfig(level=logging.DEBUG)
s = Sudo(server_url="https://example.com", debug_logger=logging.getLogger("sudo_ai"))
```

You can also enable a default debug logger by setting an environment variable `SUDO_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=sudo&utm_campaign=python)
