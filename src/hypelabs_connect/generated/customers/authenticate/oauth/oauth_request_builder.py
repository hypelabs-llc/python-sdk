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
    from ....models.authenticate_customer_o_auth_request import AuthenticateCustomerOAuthRequest
    from ....models.customer_auth_response import CustomerAuthResponse

class OauthRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /customers/authenticate/oauth
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OauthRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/customers/authenticate/oauth", path_parameters)
    
    async def post(self,body: AuthenticateCustomerOAuthRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomerAuthResponse]:
        """
        Signs in one of your customers from an identity your front-end has already verified with an external provider (Google, Apple, ...). Links the provider to an existing customer with the same email, or creates one, and returns the customer's identity.
        param body: Identity attested by an external provider (Google, GitHub, Apple, ...) after the organization's own front-end(or app) completed the OAuth sign-in. The Connect API trusts the attested identity — it never talks to theprovider itself — and finds or creates the matching customer, scoped to the calling organization.
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
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.customer_auth_response import CustomerAuthResponse

        return await self.request_adapter.send_async(request_info, CustomerAuthResponse, error_mapping)
    
    def to_post_request_information(self,body: AuthenticateCustomerOAuthRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Signs in one of your customers from an identity your front-end has already verified with an external provider (Google, Apple, ...). Links the provider to an existing customer with the same email, or creates one, and returns the customer's identity.
        param body: Identity attested by an external provider (Google, GitHub, Apple, ...) after the organization's own front-end(or app) completed the OAuth sign-in. The Connect API trusts the attested identity — it never talks to theprovider itself — and finds or creates the matching customer, scoped to the calling organization.
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
    
    def with_url(self,raw_url: str) -> OauthRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OauthRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OauthRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class OauthRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

