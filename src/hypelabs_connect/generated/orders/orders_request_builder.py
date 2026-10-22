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
    from ..models.api_response import ApiResponse
    from ..models.create_order_request import CreateOrderRequest
    from ..models.create_order_response import CreateOrderResponse
    from ..models.order import Order
    from .item.orders_item_request_builder import OrdersItemRequestBuilder
    from .preview.preview_request_builder import PreviewRequestBuilder
    from .trial.trial_request_builder import TrialRequestBuilder

class OrdersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /orders
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OrdersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/orders{?customerId*,intent*,trial*}", path_parameters)
    
    def by_id(self,id: UUID) -> OrdersItemRequestBuilder:
        """
        Gets an item from the hypelabs_connect.generated.orders.item collection
        param id: Unique identifier of the item
        Returns: OrdersItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.orders_item_request_builder import OrdersItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return OrdersItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OrdersRequestBuilderGetQueryParameters]] = None) -> Optional[list[Order]]:
        """
        Lists your active orders. Filterable by status, billing cycle, payment method, trial flag, intent (wholesale/retail), customer id, and a free-text search across all of an order's fields.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Order]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.order import Order

        return await self.request_adapter.send_collection_async(request_info, Order, None)
    
    async def post(self,body: CreateOrderRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CreateOrderResponse]:
        """
        Prices the selection and records the order.
        param body: Order request: the same selection as a price preview, plus whether it auto-renews.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreateOrderResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ApiResponse,
            "404": ApiResponse,
            "500": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.create_order_response import CreateOrderResponse

        return await self.request_adapter.send_async(request_info, CreateOrderResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OrdersRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Lists your active orders. Filterable by status, billing cycle, payment method, trial flag, intent (wholesale/retail), customer id, and a free-text search across all of an order's fields.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: CreateOrderRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Prices the selection and records the order.
        param body: Order request: the same selection as a price preview, plus whether it auto-renews.
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
    
    def with_url(self,raw_url: str) -> OrdersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OrdersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OrdersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def preview(self) -> PreviewRequestBuilder:
        """
        The preview property
        """
        from .preview.preview_request_builder import PreviewRequestBuilder

        return PreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trial(self) -> TrialRequestBuilder:
        """
        The trial property
        """
        from .trial.trial_request_builder import TrialRequestBuilder

        return TrialRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OrdersRequestBuilderGetQueryParameters():
        """
        Lists your active orders. Filterable by status, billing cycle, payment method, trial flag, intent (wholesale/retail), customer id, and a free-text search across all of an order's fields.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "customer_id":
                return "customerId"
            if original_name == "intent":
                return "intent"
            if original_name == "trial":
                return "trial"
            return original_name
        
        # Filter by the customer the order belongs to.
        customer_id: Optional[str] = None

        # Filter by order intent (wholesale or retail).
        intent: Optional[str] = None

        # Filter by trial flag.
        trial: Optional[str] = None

    
    @dataclass
    class OrdersRequestBuilderGetRequestConfiguration(RequestConfiguration[OrdersRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OrdersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

