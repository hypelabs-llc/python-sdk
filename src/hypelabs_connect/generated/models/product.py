from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .pricing_types import PricingTypes
    from .product_kinds import ProductKinds

@dataclass
class Product(AdditionalDataHolder, Parsable):
    """
    A catalog product: the shared catalog-option shape (id, stock, price, availability) plus the    product's own metadata. Internal shape (operating modes, price rows, granularity) stays on the    `Entities.Product` entity.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Count of proxies currently available (active and unallocated) behind this option.
    available_proxies: Optional[int] = None
    # Catalog list price of the option, before the organization's commercial terms. Shown as the struck-through reference next to decimal CatalogOption.Price.
    base_price: Optional[float] = None
    # Short marketing description of the product shown in the catalog.
    description: Optional[str] = None
    # Unique identifier of the catalog option.
    id: Optional[UUID] = None
    # Whether the current organization has hidden this option from its storefront.
    is_disabled: Optional[bool] = None
    # Kind of resource this product delivers (proxy, host).
    kind: Optional[ProductKinds] = None
    # Display name of the option (ISP, datacenter, capability or product name; a location uses its city or country).
    name: Optional[str] = None
    # Price the organization pays for this option: its custom override when set, otherwise the base price after its reseller discount.
    price: Optional[float] = None
    # How the product is billed.
    pricing_type: Optional[PricingTypes] = None
    # Price the organization resells this option at to its own customers (its decimal CatalogOption.Price plus margin), shown on the white-label store.
    retail_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Product:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Product
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Product()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pricing_types import PricingTypes
        from .product_kinds import ProductKinds

        from .pricing_types import PricingTypes
        from .product_kinds import ProductKinds

        fields: dict[str, Callable[[Any], None]] = {
            "availableProxies": lambda n : setattr(self, 'available_proxies', n.get_int_value()),
            "basePrice": lambda n : setattr(self, 'base_price', n.get_float_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isDisabled": lambda n : setattr(self, 'is_disabled', n.get_bool_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(ProductKinds)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "pricingType": lambda n : setattr(self, 'pricing_type', n.get_enum_value(PricingTypes)),
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
        writer.write_str_value("description", self.description)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isDisabled", self.is_disabled)
        writer.write_enum_value("kind", self.kind)
        writer.write_str_value("name", self.name)
        writer.write_float_value("price", self.price)
        writer.write_enum_value("pricingType", self.pricing_type)
        writer.write_float_value("retailPrice", self.retail_price)
        writer.write_additional_data_value(self.additional_data)
    

