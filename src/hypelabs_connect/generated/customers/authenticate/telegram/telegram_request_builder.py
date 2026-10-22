from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.api_response import ApiResponse
    from ....models.authenticate_customer_telegram_request import AuthenticateCustomerTelegramRequest
    from ....models.customer_auth_response import CustomerAuthResponse

class TelegramRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /customers/authenticate/telegram
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TelegramRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/customers/authenticate/telegram", path_parameters)
    
    async def post(self,body: AuthenticateCustomerTelegramRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomerAuthResponse]:
        """
        Signs in the customer linked to a Telegram account, for your Telegram bot. The Telegram user id is trusted as reported by the Bot API. Returns the customer's identity, or fails when no customer is linked to this Telegram account.
        param body: Identity attested by Telegram after a customer started the organization's bot. The Telegram user id is trustedas-is (Telegram authenticates it; it cannot be forged), and the Connect API resolves the customer alreadylinked to it. No customer is created here: the link is established elsewhere, by a signed-in customer addingtheir Telegram account, so an unlinked user is rejected rather than silently given a fresh account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomerAuthResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "403": ApiResponse,
            "404": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.customer_auth_response import CustomerAuthResponse

        return await self.request_adapter.send_async(request_info, CustomerAuthResponse, error_mapping)
    
    def to_post_request_information(self,body: AuthenticateCustomerTelegramRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Signs in the customer linked to a Telegram account, for your Telegram bot. The Telegram user id is trusted as reported by the Bot API. Returns the customer's identity, or fails when no customer is linked to this Telegram account.
        param body: Identity attested by Telegram after a customer started the organization's bot. The Telegram user id is trustedas-is (Telegram authenticates it; it cannot be forged), and the Connect API resolves the customer alreadylinked to it. No customer is created here: the link is established elsewhere, by a signed-in customer addingtheir Telegram account, so an unlinked user is rejected rather than silently given a fresh account.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> TelegramRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TelegramRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TelegramRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TelegramRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

