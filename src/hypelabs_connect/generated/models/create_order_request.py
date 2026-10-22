from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .order_criteria import OrderCriteria
    from .order_intents import OrderIntents

@dataclass
class CreateOrderRequest(AdditionalDataHolder, Parsable):
    """
    Order request: the same selection as a price preview, plus whether it auto-renews.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Priced selection the order is placed against.
    criteria: Optional[OrderCriteria] = None
    # The organization's end customer this order is for. Required for a retail order (it bills that customer on    the organization's connected account); must be null for wholesale (the organization itself is billed).
    customer_id: Optional[UUID] = None
    # Your own reference for this order, unique within your organization. Attach it to make creation    idempotent: a request that times out can be safely retried with the same reference and returns the order that    was already placed instead of creating a duplicate. Optional.
    external_reference: Optional[str] = None
    # The intent property
    intent: Optional[OrderIntents] = None
    # Whether the order renews itself for another billing cycle at expiry instead of lapsing. Defaults to false.
    is_auto_renew: Optional[bool] = None
    # Number of units to order. Defaults to 1.
    quantity: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateOrderRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateOrderRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateOrderRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .order_criteria import OrderCriteria
        from .order_intents import OrderIntents

        from .order_criteria import OrderCriteria
        from .order_intents import OrderIntents

        fields: dict[str, Callable[[Any], None]] = {
            "criteria": lambda n : setattr(self, 'criteria', n.get_object_value(OrderCriteria)),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_uuid_value()),
            "externalReference": lambda n : setattr(self, 'external_reference', n.get_str_value()),
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(OrderIntents)),
            "isAutoRenew": lambda n : setattr(self, 'is_auto_renew', n.get_bool_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_int_value()),
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
        writer.write_object_value("criteria", self.criteria)
        writer.write_uuid_value("customerId", self.customer_id)
        writer.write_str_value("externalReference", self.external_reference)
        writer.write_enum_value("intent", self.intent)
        writer.write_bool_value("isAutoRenew", self.is_auto_renew)
        writer.write_int_value("quantity", self.quantity)
        writer.write_additional_data_value(self.additional_data)
    

