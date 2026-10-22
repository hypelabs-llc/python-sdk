from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class CreateReviewRequest(AdditionalDataHolder, Parsable):
    """
    Payload to create a customer review.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Body text of the review.
    content: Optional[str] = None
    # Display name for the reviewer, overriding the customer name or standing in for an anonymous review.
    custom_author_name: Optional[str] = None
    # Identifier of the customer who left the review. Null for anonymous reviews.
    customer_id: Optional[UUID] = None
    # Whether the review is highlighted (for example pinned on a landing page). Defaults to false.
    is_featured: Optional[bool] = None
    # The star rating, from 1 to 5.
    rating: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateReviewRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateReviewRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateReviewRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "customAuthorName": lambda n : setattr(self, 'custom_author_name', n.get_str_value()),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_uuid_value()),
            "isFeatured": lambda n : setattr(self, 'is_featured', n.get_bool_value()),
            "rating": lambda n : setattr(self, 'rating', n.get_int_value()),
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
        writer.write_str_value("content", self.content)
        writer.write_str_value("customAuthorName", self.custom_author_name)
        writer.write_uuid_value("customerId", self.customer_id)
        writer.write_bool_value("isFeatured", self.is_featured)
        writer.write_int_value("rating", self.rating)
        writer.write_additional_data_value(self.additional_data)
    

