<!-- Start SDK Example Usage [usage] -->
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