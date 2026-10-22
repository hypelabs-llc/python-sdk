from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .billing_cycles import BillingCycles
    from .capability_types import CapabilityTypes
    from .payment_methods import PaymentMethods

@dataclass
class OrderCriteria(AdditionalDataHolder, Parsable):
    """
    Everything that narrows a product's price and stock: the order-cascade selection (Location → ISP → Datacenter),the required capabilities, and the billing cycle and payment method. Shared by the catalog facets and theorder flow. A null dimension widens the scope; it carries no validation itself. Callers enforce the chain(a level requires all its parents) with the catalog's chain guards.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billingCycle property
    billing_cycle: Optional[BillingCycles] = None
    # Capabilities the product must provide to match.
    capabilities: Optional[list[CapabilityTypes]] = None
    # ISO 3166-1 alpha-2 country code of the selected location, resolved from Guid? OrderCriteria.LocationId so a country-level price row can match. Null until resolved.
    country_code: Optional[str] = None
    # Identifier of the selected datacenter in the order cascade.
    datacenter_id: Optional[UUID] = None
    # Identifier of the selected ISP in the order cascade.
    isp_id: Optional[UUID] = None
    # Identifier of the selected location in the order cascade.
    location_id: Optional[UUID] = None
    # The paymentMethod property
    payment_method: Optional[PaymentMethods] = None
    # Identifier of the product being priced or ordered.
    product_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrderCriteria:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrderCriteria
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrderCriteria()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_cycles import BillingCycles
        from .capability_types import CapabilityTypes
        from .payment_methods import PaymentMethods

        from .billing_cycles import BillingCycles
        from .capability_types import CapabilityTypes
        from .payment_methods import PaymentMethods

        fields: dict[str, Callable[[Any], None]] = {
            "billingCycle": lambda n : setattr(self, 'billing_cycle', n.get_enum_value(BillingCycles)),
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_collection_of_enum_values(CapabilityTypes)),
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "datacenterId": lambda n : setattr(self, 'datacenter_id', n.get_uuid_value()),
            "ispId": lambda n : setattr(self, 'isp_id', n.get_uuid_value()),
            "locationId": lambda n : setattr(self, 'location_id', n.get_uuid_value()),
            "paymentMethod": lambda n : setattr(self, 'payment_method', n.get_enum_value(PaymentMethods)),
            "productId": lambda n : setattr(self, 'product_id', n.get_uuid_value()),
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
        writer.write_enum_value("billingCycle", self.billing_cycle)
        writer.write_collection_of_enum_values("capabilities", self.capabilities)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_uuid_value("datacenterId", self.datacenter_id)
        writer.write_uuid_value("ispId", self.isp_id)
        writer.write_uuid_value("locationId", self.location_id)
        writer.write_enum_value("paymentMethod", self.payment_method)
        writer.write_uuid_value("productId", self.product_id)
        writer.write_additional_data_value(self.additional_data)
    

