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
    from ...models.proxy import Proxy
    from .annotations.annotations_request_builder import AnnotationsRequestBuilder
    from .credentials.credentials_request_builder import CredentialsRequestBuilder
    from .ip_info.ip_info_request_builder import IpInfoRequestBuilder
    from .ip_rotation.ip_rotation_request_builder import IpRotationRequestBuilder
    from .options.options_request_builder import OptionsRequestBuilder
    from .ping.ping_request_builder import PingRequestBuilder

class WithProxyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /proxies/{proxyId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithProxyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/proxies/{proxyId}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Proxy]:
        """
        Returns one of your proxies with its connection details.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Proxy]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.proxy import Proxy

        return await self.request_adapter.send_async(request_info, Proxy, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns one of your proxies with its connection details.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> WithProxyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithProxyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithProxyItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def annotations(self) -> AnnotationsRequestBuilder:
        """
        The annotations property
        """
        from .annotations.annotations_request_builder import AnnotationsRequestBuilder

        return AnnotationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def credentials(self) -> CredentialsRequestBuilder:
        """
        The credentials property
        """
        from .credentials.credentials_request_builder import CredentialsRequestBuilder

        return CredentialsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ip_info(self) -> IpInfoRequestBuilder:
        """
        The ipInfo property
        """
        from .ip_info.ip_info_request_builder import IpInfoRequestBuilder

        return IpInfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ip_rotation(self) -> IpRotationRequestBuilder:
        """
        The ipRotation property
        """
        from .ip_rotation.ip_rotation_request_builder import IpRotationRequestBuilder

        return IpRotationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def options_path(self) -> OptionsRequestBuilder:
        """
        The optionsPath property
        """
        from .options.options_request_builder import OptionsRequestBuilder

        return OptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ping(self) -> PingRequestBuilder:
        """
        The ping property
        """
        from .ping.ping_request_builder import PingRequestBuilder

        return PingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithProxyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

