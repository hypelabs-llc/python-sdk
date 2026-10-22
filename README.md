<p align="center">
  <img src="https://i.imgur.com/NtKvmk2.png" height="100" alt="HypeLabs" />
</p>
<h3 align="center">
  HypeLabs Connect SDK
</h3>
<p align="center">
  The Python client for the HypeLabs Connect API.
</p>
<p align="center">
  <a href="https://pypi.org/project/hypelabs-connect/"><img src="https://img.shields.io/pypi/v/hypelabs-connect?color=3775a9&label=pypi" /></a>
  <a href="https://pypi.org/project/hypelabs-connect/"><img src="https://img.shields.io/pypi/dm/hypelabs-connect?color=3775a9&label=Downloads" /></a>
  <a href="https://connect.hypelabs.network"><img src="https://img.shields.io/badge/API-connect.hypelabs.network-6366f1" /></a>
  <a href="https://learn.microsoft.com/openapi/kiota/"><img src="https://img.shields.io/badge/Generated%20With-Kiota-0078d4" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" /></a>
</p>

## Requirements

- Python 3.10 or later
- A HypeLabs Connect API key (`hl_live_…`)

> The client authenticates with an API key, so run it **server-side** (a backend or a job) — never ship your
> key to a browser or a client app.

## Install

1. **Add the package:**

   ```bash
   pip install hypelabs-connect
   ```

2. **Create your organization** on the [HypeLabs Console](https://console.hypelabs.network/?utm_source=github&utm_medium=readme&utm_campaign=python-sdk) and generate an API key.

## Usage

Create a client with your API key and call the API. Every call is async and returns typed models.

```python
import asyncio
from hypelabs_connect import create_connect_client

client = create_connect_client("hl_live_...")


async def main():
    proxies = await client.proxies.get()
    for proxy in proxies or []:
        print(proxy.id)


asyncio.run(main())
```

The API is authenticated with the `X-Api-Key` header, wired up internally — you never touch the Kiota plumbing.
