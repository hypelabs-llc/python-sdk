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
    from ....models.proxy_ip_rotation_response import ProxyIpRotationResponse
    from ....models.update_proxy_ip_rotation_request import UpdateProxyIpRotationRequest
    from .link.link_request_builder import LinkRequestBuilder
    from .trigger.trigger_request_builder import TriggerRequestBuilder

class IpRotationRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /proxies/{proxyId}/ip-rotation
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IpRotationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/proxies/{proxyId}/ip-rotation", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ProxyIpRotationResponse]:
        """
        Returns the IP rotation configured on an owned proxy.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ProxyIpRotationResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.proxy_ip_rotation_response import ProxyIpRotationResponse

        return await self.request_adapter.send_async(request_info, ProxyIpRotationResponse, None)
    
    async def put(self,body: UpdateProxyIpRotationRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Configures how often the proxy rotates its IP. An interval of 0 disables rotation.
        param body: Request to configure a proxy's IP rotation. An interval of 0 disables rotation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the IP rotation configured on an owned proxy.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: UpdateProxyIpRotationRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Configures how often the proxy rotates its IP. An interval of 0 disables rotation.
        param body: Request to configure a proxy's IP rotation. An interval of 0 disables rotation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> IpRotationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IpRotationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IpRotationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def link(self) -> LinkRequestBuilder:
        """
        The link property
        """
        from .link.link_request_builder import LinkRequestBuilder

        return LinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trigger(self) -> TriggerRequestBuilder:
        """
        The trigger property
        """
        from .trigger.trigger_request_builder import TriggerRequestBuilder

        return TriggerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IpRotationRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IpRotationRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

