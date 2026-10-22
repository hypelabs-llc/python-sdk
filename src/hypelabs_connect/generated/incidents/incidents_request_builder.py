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
    from ..models.create_incident_request import CreateIncidentRequest
    from ..models.incident import Incident
    from .item.with_incident_item_request_builder import WithIncidentItemRequestBuilder

class IncidentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /incidents
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IncidentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/incidents{?reporter*,status*}", path_parameters)
    
    def by_incident_id(self,incident_id: UUID) -> WithIncidentItemRequestBuilder:
        """
        Gets an item from the hypelabs_connect.generated.incidents.item collection
        param incident_id: Unique identifier of the item
        Returns: WithIncidentItemRequestBuilder
        """
        if incident_id is None:
            raise TypeError("incident_id cannot be null.")
        from .item.with_incident_item_request_builder import WithIncidentItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["incidentId"] = incident_id
        return WithIncidentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IncidentsRequestBuilderGetQueryParameters]] = None) -> Optional[list[Incident]]:
        """
        Returns the incidents reported for your organization, most recent first.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Incident]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.incident import Incident

        return await self.request_adapter.send_collection_async(request_info, Incident, None)
    
    async def post(self,body: CreateIncidentRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Incident]:
        """
        Reports a new incident for your organization. Rejected with 409 if an incident is already open for the same target.
        param body: Payload to open a new incident.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Incident]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "409": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.incident import Incident

        return await self.request_adapter.send_async(request_info, Incident, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IncidentsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the incidents reported for your organization, most recent first.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: CreateIncidentRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Reports a new incident for your organization. Rejected with 409 if an incident is already open for the same target.
        param body: Payload to open a new incident.
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
    
    def with_url(self,raw_url: str) -> IncidentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IncidentsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IncidentsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class IncidentsRequestBuilderGetQueryParameters():
        """
        Returns the incidents reported for your organization, most recent first.
        """
        # Filter by reporter email.
        reporter: Optional[str] = None

        # Filter by incident status.
        status: Optional[str] = None

    
    @dataclass
    class IncidentsRequestBuilderGetRequestConfiguration(RequestConfiguration[IncidentsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IncidentsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

