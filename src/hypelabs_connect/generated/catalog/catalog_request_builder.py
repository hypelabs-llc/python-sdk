from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .capabilities.capabilities_request_builder import CapabilitiesRequestBuilder
    from .datacenters.datacenters_request_builder import DatacentersRequestBuilder
    from .isps.isps_request_builder import IspsRequestBuilder
    from .locations.locations_request_builder import LocationsRequestBuilder
    from .products.products_request_builder import ProductsRequestBuilder

class CatalogRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /catalog
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CatalogRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/catalog", path_parameters)
    
    @property
    def capabilities(self) -> CapabilitiesRequestBuilder:
        """
        The capabilities property
        """
        from .capabilities.capabilities_request_builder import CapabilitiesRequestBuilder

        return CapabilitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def datacenters(self) -> DatacentersRequestBuilder:
        """
        The datacenters property
        """
        from .datacenters.datacenters_request_builder import DatacentersRequestBuilder

        return DatacentersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def isps(self) -> IspsRequestBuilder:
        """
        The isps property
        """
        from .isps.isps_request_builder import IspsRequestBuilder

        return IspsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def locations(self) -> LocationsRequestBuilder:
        """
        The locations property
        """
        from .locations.locations_request_builder import LocationsRequestBuilder

        return LocationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def products(self) -> ProductsRequestBuilder:
        """
        The products property
        """
        from .products.products_request_builder import ProductsRequestBuilder

        return ProductsRequestBuilder(self.request_adapter, self.path_parameters)
    

