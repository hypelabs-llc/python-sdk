from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class Isp(AdditionalDataHolder, Parsable):
    """
    Internet service provider a proxy routes through.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Count of proxies currently available (active and unallocated) behind this option.
    available_proxies: Optional[int] = None
    # Catalog list price of the option, before the organization's commercial terms. Shown as the struck-through reference next to decimal CatalogOption.Price.
    base_price: Optional[float] = None
    # Unique identifier of the catalog option.
    id: Optional[UUID] = None
    # Whether the current organization has hidden this option from its storefront.
    is_disabled: Optional[bool] = None
    # Absolute URL of the ISP logo, null when none is set.
    logo_url: Optional[str] = None
    # Display name of the option (ISP, datacenter, capability or product name; a location uses its city or country).
    name: Optional[str] = None
    # Price the organization pays for this option: its custom override when set, otherwise the base price after its reseller discount.
    price: Optional[float] = None
    # Price the organization resells this option at to its own customers (its decimal CatalogOption.Price plus margin), shown on the white-label store.
    retail_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Isp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Isp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Isp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "availableProxies": lambda n : setattr(self, 'available_proxies', n.get_int_value()),
            "basePrice": lambda n : setattr(self, 'base_price', n.get_float_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isDisabled": lambda n : setattr(self, 'is_disabled', n.get_bool_value()),
            "logoUrl": lambda n : setattr(self, 'logo_url', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "retailPrice": lambda n : setattr(self, 'retail_price', n.get_float_value()),
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
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isDisabled", self.is_disabled)
        writer.write_str_value("logoUrl", self.logo_url)
        writer.write_str_value("name", self.name)
        writer.write_float_value("price", self.price)
        writer.write_float_value("retailPrice", self.retail_price)
        writer.write_additional_data_value(self.additional_data)
    

