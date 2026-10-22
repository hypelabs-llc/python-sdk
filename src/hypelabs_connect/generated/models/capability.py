from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .capability_types import CapabilityTypes

@dataclass
class Capability(AdditionalDataHolder, Parsable):
    """
    A catalog capability that proxies can expose (IPv6, IP scoring, and similar features).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Count of proxies currently available (active and unallocated) behind this option.
    available_proxies: Optional[int] = None
    # Catalog list price of the option, before the organization's commercial terms. Shown as the struck-through reference next to decimal CatalogOption.Price.
    base_price: Optional[float] = None
    # Human-readable explanation of what the capability provides. Null when none is set.
    description: Optional[str] = None
    # Unique identifier of the catalog option.
    id: Optional[UUID] = None
    # Whether the current organization has hidden this option from its storefront.
    is_disabled: Optional[bool] = None
    # Display name of the option (ISP, datacenter, capability or product name; a location uses its city or country).
    name: Optional[str] = None
    # Price the organization pays for this option: its custom override when set, otherwise the base price after its reseller discount.
    price: Optional[float] = None
    # Price the organization resells this option at to its own customers (its decimal CatalogOption.Price plus margin), shown on the white-label store.
    retail_price: Optional[float] = None
    # Which capability this option is (e.g. IPv6, IP scoring).
    type: Optional[CapabilityTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Capability:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Capability
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Capability()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .capability_types import CapabilityTypes

        from .capability_types import CapabilityTypes

        fields: dict[str, Callable[[Any], None]] = {
            "availableProxies": lambda n : setattr(self, 'available_proxies', n.get_int_value()),
            "basePrice": lambda n : setattr(self, 'base_price', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isDisabled": lambda n : setattr(self, 'is_disabled', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "retailPrice": lambda n : setattr(self, 'retail_price', n.get_float_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CapabilityTypes)),
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
        writer.write_int_value("availableProxies", self.available_proxies)
        writer.write_float_value("basePrice", self.base_price)
        writer.write_str_value("description", self.description)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isDisabled", self.is_disabled)
        writer.write_str_value("name", self.name)
        writer.write_float_value("price", self.price)
        writer.write_float_value("retailPrice", self.retail_price)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

