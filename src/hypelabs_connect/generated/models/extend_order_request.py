from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .billing_cycles import BillingCycles
    from .payment_methods import PaymentMethods

@dataclass
class ExtendOrderRequest(AdditionalDataHolder, Parsable):
    """
    Renews an existing order for another billing cycle, optionally on different terms.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billingCycle property
    billing_cycle: Optional[BillingCycles] = None
    # The paymentMethod property
    payment_method: Optional[PaymentMethods] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ExtendOrderRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ExtendOrderRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ExtendOrderRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_cycles import BillingCycles
        from .payment_methods import PaymentMethods

        from .billing_cycles import BillingCycles
        from .payment_methods import PaymentMethods

        fields: dict[str, Callable[[Any], None]] = {
            "billingCycle": lambda n : setattr(self, 'billing_cycle', n.get_enum_value(BillingCycles)),
            "paymentMethod": lambda n : setattr(self, 'payment_method', n.get_enum_value(PaymentMethods)),
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
        writer.write_enum_value("paymentMethod", self.payment_method)
        writer.write_additional_data_value(self.additional_data)
    

