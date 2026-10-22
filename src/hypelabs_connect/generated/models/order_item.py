from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .order_item_metadata import OrderItem_metadata
    from .product_kinds import ProductKinds

@dataclass
class OrderItem(AdditionalDataHolder, Parsable):
    """
    One line of an Order? OrderItem.Order: a product bought in a given quantity, with the resources delivered for it.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The id property
    id: Optional[UUID] = None
    # Kind of resource this line's product delivers (proxy or host).
    kind: Optional[ProductKinds] = None
    # The metadata property
    metadata: Optional[OrderItem_metadata] = None
    # Identifier of the product this line orders.
    product_id: Optional[UUID] = None
    # Identifiers of the resources delivered for this line (proxy ids today), resolved against the cached stock. Null until the order is placed and its resources are provisioned.
    resource_ids: Optional[list[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrderItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrderItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrderItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .order_item_metadata import OrderItem_metadata
        from .product_kinds import ProductKinds

        from .order_item_metadata import OrderItem_metadata
        from .product_kinds import ProductKinds

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(ProductKinds)),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(OrderItem_metadata)),
            "productId": lambda n : setattr(self, 'product_id', n.get_uuid_value()),
            "resourceIds": lambda n : setattr(self, 'resource_ids', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_uuid_value("id", self.id)
        writer.write_enum_value("kind", self.kind)
        writer.write_object_value("metadata", self.metadata)
        writer.write_uuid_value("productId", self.product_id)
        writer.write_collection_of_primitive_values("resourceIds", self.resource_ids)
        writer.write_additional_data_value(self.additional_data)
    

