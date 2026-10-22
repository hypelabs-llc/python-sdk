from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .api_error import ApiError
    from .request_details import RequestDetails

from .api_error import ApiError

@dataclass
class ApiResponse(APIError, AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The errors property
    errors: Optional[list[ApiError]] = None
    # The message property
    message: Optional[str] = None
    # The requestDetails property
    request_details: Optional[RequestDetails] = None
    # The statusCode property
    status_code: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ApiResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ApiResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ApiResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .api_error import ApiError
        from .request_details import RequestDetails

        from .api_error import ApiError
        from .request_details import RequestDetails

        fields: dict[str, Callable[[Any], None]] = {
            "errors": lambda n : setattr(self, 'errors', n.get_collection_of_object_values(ApiError)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "requestDetails": lambda n : setattr(self, 'request_details', n.get_object_value(RequestDetails)),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_object_values("errors", self.errors)
        writer.write_str_value("message", self.message)
        writer.write_object_value("requestDetails", self.request_details)
        writer.write_int_value("statusCode", self.status_code)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

