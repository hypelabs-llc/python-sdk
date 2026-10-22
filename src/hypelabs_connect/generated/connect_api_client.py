from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from kiota_serialization_form.form_parse_node_factory import FormParseNodeFactory
from kiota_serialization_form.form_serialization_writer_factory import FormSerializationWriterFactory
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import JsonSerializationWriterFactory
from kiota_serialization_multipart.multipart_serialization_writer_factory import MultipartSerializationWriterFactory
from kiota_serialization_text.text_parse_node_factory import TextParseNodeFactory
from kiota_serialization_text.text_serialization_writer_factory import TextSerializationWriterFactory
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .announcements.announcements_request_builder import AnnouncementsRequestBuilder
    from .catalog.catalog_request_builder import CatalogRequestBuilder
    from .customers.customers_request_builder import CustomersRequestBuilder
    from .incidents.incidents_request_builder import IncidentsRequestBuilder
    from .orders.orders_request_builder import OrdersRequestBuilder
    from .proxies.proxies_request_builder import ProxiesRequestBuilder
    from .reviews.reviews_request_builder import ReviewsRequestBuilder

class ConnectApiClient(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new ConnectApiClient and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        register_default_serializer(JsonSerializationWriterFactory)
        register_default_serializer(TextSerializationWriterFactory)
        register_default_serializer(FormSerializationWriterFactory)
        register_default_serializer(MultipartSerializationWriterFactory)
        register_default_deserializer(JsonParseNodeFactory)
        register_default_deserializer(TextParseNodeFactory)
        register_default_deserializer(FormParseNodeFactory)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://connect.hypelabs.network"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def announcements(self) -> AnnouncementsRequestBuilder:
        """
        The announcements property
        """
        from .announcements.announcements_request_builder import AnnouncementsRequestBuilder

        return AnnouncementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def catalog(self) -> CatalogRequestBuilder:
        """
        The catalog property
        """
        from .catalog.catalog_request_builder import CatalogRequestBuilder

        return CatalogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customers(self) -> CustomersRequestBuilder:
        """
        The customers property
        """
        from .customers.customers_request_builder import CustomersRequestBuilder

        return CustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def incidents(self) -> IncidentsRequestBuilder:
        """
        The incidents property
        """
        from .incidents.incidents_request_builder import IncidentsRequestBuilder

        return IncidentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def orders(self) -> OrdersRequestBuilder:
        """
        The orders property
        """
        from .orders.orders_request_builder import OrdersRequestBuilder

        return OrdersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def proxies(self) -> ProxiesRequestBuilder:
        """
        The proxies property
        """
        from .proxies.proxies_request_builder import ProxiesRequestBuilder

        return ProxiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reviews(self) -> ReviewsRequestBuilder:
        """
        The reviews property
        """
        from .reviews.reviews_request_builder import ReviewsRequestBuilder

        return ReviewsRequestBuilder(self.request_adapter, self.path_parameters)
    

