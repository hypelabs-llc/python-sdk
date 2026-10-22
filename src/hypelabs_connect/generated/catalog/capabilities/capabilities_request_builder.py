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
    from ...models.capability import Capability

class CapabilitiesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /catalog/capabilities
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CapabilitiesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/catalog/capabilities{?datacenterId*,ispId*,locationId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[CapabilitiesRequestBuilderGetQueryParameters]] = None) -> Optional[list[Capability]]:
        """
        Returns the sellable proxy capabilities (title, description, icon) with their stock for the selection.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Capability]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.capability import Capability

        return await self.request_adapter.send_collection_async(request_info, Capability, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[CapabilitiesRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the sellable proxy capabilities (title, description, icon) with their stock for the selection.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> CapabilitiesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CapabilitiesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CapabilitiesRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CapabilitiesRequestBuilderGetQueryParameters():
        """
        Returns the sellable proxy capabilities (title, description, icon) with their stock for the selection.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "datacenter_id":
                return "datacenterId"
            if original_name == "isp_id":
                return "ispId"
            if original_name == "location_id":
                return "locationId"
            return original_name
        
        # Narrow the stock to this datacenter (optional).
        datacenter_id: Optional[UUID] = None

        # Narrow the stock to this ISP (optional).
        isp_id: Optional[UUID] = None

        # Narrow the stock to this location (optional).
        location_id: Optional[UUID] = None

    
    @dataclass
    class CapabilitiesRequestBuilderGetRequestConfiguration(RequestConfiguration[CapabilitiesRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

