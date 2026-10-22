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
    from ...models.api_response import ApiResponse
    from ...models.cancel_order_request import CancelOrderRequest
    from ...models.order import Order
    from .extend.extend_request_builder import ExtendRequestBuilder
    from .proxies.proxies_request_builder import ProxiesRequestBuilder

class OrdersItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /orders/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OrdersItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/orders/{id}", path_parameters)
    
    async def delete(self,body: CancelOrderRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Stops the order renewing (cancelling its subscription when it has one). By default the paid period is kept until expiry; set immediateCancellation to end it now. Set askRefund to also refund the latest payment when still within the refund window.
        param body: Cancels an order: how to end its billing and whether to refund.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        from ...models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": ApiResponse,
            "409": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Order]:
        """
        Returns one of your orders by id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Order]
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
        from ...models.order import Order

        return await self.request_adapter.send_async(request_info, Order, error_mapping)
    
    def to_delete_request_information(self,body: CancelOrderRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Stops the order renewing (cancelling its subscription when it has one). By default the paid period is kept until expiry; set immediateCancellation to end it now. Set askRefund to also refund the latest payment when still within the refund window.
        param body: Cancels an order: how to end its billing and whether to refund.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns one of your orders by id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> OrdersItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OrdersItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OrdersItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def extend(self) -> ExtendRequestBuilder:
        """
        The extend property
        """
        from .extend.extend_request_builder import ExtendRequestBuilder

        return ExtendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def proxies(self) -> ProxiesRequestBuilder:
        """
        The proxies property
        """
        from .proxies.proxies_request_builder import ProxiesRequestBuilder

        return ProxiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OrdersItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OrdersItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

