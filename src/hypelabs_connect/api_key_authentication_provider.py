from __future__ import annotations

from kiota_abstractions.authentication import AuthenticationProvider
from kiota_abstractions.request_information import RequestInformation


class ApiKeyAuthenticationProvider(AuthenticationProvider):
    """Authenticates every request with the Connect API's ``X-Api-Key`` header. Kiota calls this before each
    outgoing request; the key is supplied once when the client is created."""

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key

    async def authenticate_request(
        self, request: RequestInformation, additional_authentication_context: dict | None = None
    ) -> None:
        request.headers.try_add("X-Api-Key", self._api_key)
