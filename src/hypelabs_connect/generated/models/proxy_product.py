from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .product_kinds import ProductKinds

@dataclass
class ProxyProduct(AdditionalDataHolder, Parsable):
    """
    The catalog product a proxy was ordered as: the head of the cascade down to location, ISP and    datacenter.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the product, to refetch or reorder it.
    id: Optional[UUID] = None
    # Kind of resource the product delivers (proxy, host).
    kind: Optional[ProductKinds] = None
    # Name of the product.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProxyProduct:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxyProduct
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProxyProduct()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .product_kinds import ProductKinds

        from .product_kinds import ProductKinds

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(ProductKinds)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

