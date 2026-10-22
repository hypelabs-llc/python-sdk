from __future__ import annotations

from kiota_bundle.default_request_adapter import DefaultRequestAdapter

from .api_key_authentication_provider import ApiKeyAuthenticationProvider
from .generated.connect_api_client import ConnectApiClient


def create_connect_client(api_key: str) -> ConnectApiClient:
    """The entry point to the HypeLabs Connect API. Create one with your API key and use the fluent request
    builders it returns: ``client.proxies.get()``, ``client.customers.post(...)``, and so on.

    .. code-block:: python

        client = create_connect_client("hl_live_...")
        proxies = await client.proxies.get()

    The request adapter and the ``X-Api-Key`` authentication are wired up internally, so callers never touch
    the generated Kiota plumbing directly.

    :param api_key: A Connect API key (e.g. ``hl_live_…``).
    """
    if not api_key or not api_key.strip():
        raise ValueError("An API key is required.")
    adapter = DefaultRequestAdapter(ApiKeyAuthenticationProvider(api_key))
    return ConnectApiClient(adapter)
