from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PreviewOrderResponse(AdditionalDataHolder, Parsable):
    """
    The computed price for an order selection, before it is placed.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # How many proxies are available for the selection right now.
    available_proxies: Optional[int] = None
    # ISO 4217 currency code the amounts are expressed in.
    currency: Optional[str] = None
    # Amount saved versus paying monthly for the same duration. Null when there is no saving.
    discount: Optional[float] = None
    # Saving as a percentage of the monthly-rate total, from 0 to 100. Null when there is no saving.
    discount_percent: Optional[float] = None
    # Number of units in the selection.
    quantity: Optional[int] = None
    # Unit price multiplied by quantity, before any future discounts.
    subtotal: Optional[float] = None
    # Final amount to charge (equals subtotal until discounts exist).
    total: Optional[float] = None
    # Resolved price for a single unit.
    unit_price: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PreviewOrderResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PreviewOrderResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PreviewOrderResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "availableProxies": lambda n : setattr(self, 'available_proxies', n.get_int_value()),
            "currency": lambda n : setattr(self, 'currency', n.get_str_value()),
            "discount": lambda n : setattr(self, 'discount', n.get_float_value()),
            "discountPercent": lambda n : setattr(self, 'discount_percent', n.get_float_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_int_value()),
            "subtotal": lambda n : setattr(self, 'subtotal', n.get_float_value()),
            "total": lambda n : setattr(self, 'total', n.get_float_value()),
            "unitPrice": lambda n : setattr(self, 'unit_price', n.get_float_value()),
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
        writer.write_str_value("currency", self.currency)
        writer.write_float_value("discount", self.discount)
        writer.write_float_value("discountPercent", self.discount_percent)
        writer.write_int_value("quantity", self.quantity)
        writer.write_float_value("subtotal", self.subtotal)
        writer.write_float_value("total", self.total)
        writer.write_float_value("unitPrice", self.unit_price)
        writer.write_additional_data_value(self.additional_data)
    

