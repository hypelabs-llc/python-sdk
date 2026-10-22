from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .review_metadata import Review_metadata

@dataclass
class Review(AdditionalDataHolder, Parsable):
    """
    A review left by one of an organization's customers: review text plus a star rating, owned by and scoped tothe Organization? Review.Organization. Tied to a known Customer? Review.Customer via Guid? Review.CustomerId when thereis one, otherwise left anonymous with a string? Review.CustomAuthorName.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The name to show for the reviewer: the explicit string? Review.CustomAuthorName if set, otherwise    the linked customer's display name or email, falling back to "Anonymous". Requires the customer to be    loaded (see the reads that `Include` it).
    author_name: Optional[str] = None
    # The review text.
    content: Optional[str] = None
    # Display name for the reviewer when no customer is tied to the review, or an override of the linked    customer's name. Null falls back to the Customer? Review.Customer's name.
    custom_author_name: Optional[str] = None
    # Id of the customer who left the review when it is tied to a known one, or null for anonymous reviews.
    customer_id: Optional[UUID] = None
    # The id property
    id: Optional[UUID] = None
    # Whether the review is highlighted (e.g. pinned on a landing page). Defaults to false.
    is_featured: Optional[bool] = None
    # Whether the review awaits moderation: true until approved, and only non-pending reviews show    publicly (rejecting one deletes it).
    is_pending: Optional[bool] = None
    # The metadata property
    metadata: Optional[Review_metadata] = None
    # The star rating, from 1 to 5.
    rating: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Review:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Review
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Review()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .review_metadata import Review_metadata

        from .review_metadata import Review_metadata

        fields: dict[str, Callable[[Any], None]] = {
            "authorName": lambda n : setattr(self, 'author_name', n.get_str_value()),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "customAuthorName": lambda n : setattr(self, 'custom_author_name', n.get_str_value()),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_uuid_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isFeatured": lambda n : setattr(self, 'is_featured', n.get_bool_value()),
            "isPending": lambda n : setattr(self, 'is_pending', n.get_bool_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(Review_metadata)),
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
        writer.write_str_value("authorName", self.author_name)
        writer.write_str_value("content", self.content)
        writer.write_str_value("customAuthorName", self.custom_author_name)
        writer.write_uuid_value("customerId", self.customer_id)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isFeatured", self.is_featured)
        writer.write_bool_value("isPending", self.is_pending)
        writer.write_object_value("metadata", self.metadata)
        writer.write_int_value("rating", self.rating)
        writer.write_additional_data_value(self.additional_data)
    

