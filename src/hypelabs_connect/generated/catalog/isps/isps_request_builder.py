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
from uuid import UUID
from warnings import warn

if TYPE_CHECKING:
    from ...models.api_response import ApiResponse
    from ...models.isp import Isp

class IspsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /catalog/isps
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IspsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/catalog/isps?locationId={locationId}&productId={productId}{&includeDisabled*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IspsRequestBuilderGetQueryParameters]] = None) -> Optional[list[Isp]]:
        """
        Returns the available ISPs for a product and location. Options the organization has disabled are hidden unless includeDisabled is set.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Isp]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.isp import Isp

        return await self.request_adapter.send_collection_async(request_info, Isp, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IspsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the available ISPs for a product and location. Options the organization has disabled are hidden unless includeDisabled is set.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> IspsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IspsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IspsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class IspsRequestBuilderGetQueryParameters():
        """
        Returns the available ISPs for a product and location. Options the organization has disabled are hidden unless includeDisabled is set.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_disabled":
                return "includeDisabled"
            if original_name == "location_id":
                return "locationId"
            if original_name == "product_id":
                return "productId"
            return original_name
        
        # Include options the organization has disabled (hidden by default).
        include_disabled: Optional[bool] = None

        # Identifier of the selected location.
        location_id: Optional[UUID] = None

        # Identifier of the product being priced.
        product_id: Optional[UUID] = None

    
    @dataclass
    class IspsRequestBuilderGetRequestConfiguration(RequestConfiguration[IspsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

