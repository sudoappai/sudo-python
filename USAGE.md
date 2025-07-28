<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import os
from sudo import Sudo

async def main():

    async with Sudo(
        server_url="https://api.example.com",
        api_key=os.getenv("SUDO_API_KEY", ""),
    ) as s_client:

        res = await s_client.system.health_check_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->