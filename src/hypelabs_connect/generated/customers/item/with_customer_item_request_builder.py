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
    from ...models.customer import Customer
    from ...models.patch_customer_request import PatchCustomerRequest
    from ...models.update_customer_request import UpdateCustomerRequest
    from .billing.billing_request_builder import BillingRequestBuilder
    from .defaults.defaults_request_builder import DefaultsRequestBuilder
    from .kyc.kyc_request_builder import KycRequestBuilder
    from .metadata.metadata_request_builder import MetadataRequestBuilder
    from .password.password_request_builder import PasswordRequestBuilder
    from .reset_password.reset_password_request_builder import ResetPasswordRequestBuilder
    from .send_verification.send_verification_request_builder import SendVerificationRequestBuilder

class WithCustomerItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /customers/{customerId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithCustomerItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/customers/{customerId}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Permanently deletes a customer from your organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Customer]:
        """
        Returns a single customer belonging to your organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Customer]
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
        from ...models.customer import Customer

        return await self.request_adapter.send_async(request_info, Customer, error_mapping)
    
    async def patch(self,body: PatchCustomerRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Partially updates a customer. Suspending a customer (isActive=false) blocks them from authenticating; reinstating (isActive=true) restores access.
        param body: Partial update of a customer: only the provided fields are changed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def put(self,body: UpdateCustomerRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Customer]:
        """
        Updates a customer's details. Fields left null are unchanged.
        param body: Payload to update a customer. Null fields are left unchanged.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Customer]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ...models.api_response import ApiResponse

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": ApiResponse,
            "409": ApiResponse,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.customer import Customer

        return await self.request_adapter.send_async(request_info, Customer, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Permanently deletes a customer from your organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a single customer belonging to your organization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: PatchCustomerRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Partially updates a customer. Suspending a customer (isActive=false) blocks them from authenticating; reinstating (isActive=true) restores access.
        param body: Partial update of a customer: only the provided fields are changed.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_put_request_information(self,body: UpdateCustomerRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates a customer's details. Fields left null are unchanged.
        param body: Payload to update a customer. Null fields are left unchanged.
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
    
    def with_url(self,raw_url: str) -> WithCustomerItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithCustomerItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithCustomerItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def billing(self) -> BillingRequestBuilder:
        """
        The billing property
        """
        from .billing.billing_request_builder import BillingRequestBuilder

        return BillingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def defaults(self) -> DefaultsRequestBuilder:
        """
        The defaults property
        """
        from .defaults.defaults_request_builder import DefaultsRequestBuilder

        return DefaultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def kyc(self) -> KycRequestBuilder:
        """
        The kyc property
        """
        from .kyc.kyc_request_builder import KycRequestBuilder

        return KycRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metadata(self) -> MetadataRequestBuilder:
        """
        The metadata property
        """
        from .metadata.metadata_request_builder import MetadataRequestBuilder

        return MetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def password(self) -> PasswordRequestBuilder:
        """
        The password property
        """
        from .password.password_request_builder import PasswordRequestBuilder

        return PasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_password(self) -> ResetPasswordRequestBuilder:
        """
        The resetPassword property
        """
        from .reset_password.reset_password_request_builder import ResetPasswordRequestBuilder

        return ResetPasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_verification(self) -> SendVerificationRequestBuilder:
        """
        The sendVerification property
        """
        from .send_verification.send_verification_request_builder import SendVerificationRequestBuilder

        return SendVerificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithCustomerItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCustomerItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCustomerItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithCustomerItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

