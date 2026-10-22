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
    from ..models.create_review_request import CreateReviewRequest
    from ..models.review import Review
    from .item.with_review_item_request_builder import WithReviewItemRequestBuilder

class ReviewsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /reviews
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ReviewsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reviews", path_parameters)
    
    def by_review_id(self,review_id: UUID) -> WithReviewItemRequestBuilder:
        """
        Gets an item from the hypelabs_connect.generated.reviews.item collection
        param review_id: Unique identifier of the item
        Returns: WithReviewItemRequestBuilder
        """
        if review_id is None:
            raise TypeError("review_id cannot be null.")
        from .item.with_review_item_request_builder import WithReviewItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["reviewId"] = review_id
        return WithReviewItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[Review]]:
        """
        Returns the reviews left for your organization, most recent first.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Review]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.review import Review

        return await self.request_adapter.send_collection_async(request_info, Review, None)
    
    async def post(self,body: CreateReviewRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Review]:
        """
        Adds a review for your organization, optionally tied to one of your customers.
        param body: Payload to create a customer review.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Review]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.review import Review

        return await self.request_adapter.send_async(request_info, Review, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the reviews left for your organization, most recent first.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: CreateReviewRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds a review for your organization, optionally tied to one of your customers.
        param body: Payload to create a customer review.
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
    
    def with_url(self,raw_url: str) -> ReviewsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReviewsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ReviewsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ReviewsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReviewsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

