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
    from ....models.proxy_options import ProxyOptions
    from ....models.update_proxy_options_request import UpdateProxyOptionsRequest

class OptionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /proxies/{proxyId}/options
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OptionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/proxies/{proxyId}/options", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ProxyOptions]:
        """
        Returns the feature options set on an owned proxy, or the defaults when none are set yet.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ProxyOptions]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.proxy_options import ProxyOptions

        return await self.request_adapter.send_async(request_info, ProxyOptions, None)
    
    async def put(self,body: UpdateProxyOptionsRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Sets the feature options on an owned proxy, such as its resolution mode.
        param body: The feature options to set on a proxy. A non-default option is only accepted when the proxy exposes    the capability it depends on (see ProxyOptions).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ....models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "422": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the feature options set on an owned proxy, or the defaults when none are set yet.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: UpdateProxyOptionsRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Sets the feature options on an owned proxy, such as its resolution mode.
        param body: The feature options to set on a proxy. A non-default option is only accepted when the proxy exposes    the capability it depends on (see ProxyOptions).
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> OptionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OptionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OptionsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class OptionsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OptionsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

