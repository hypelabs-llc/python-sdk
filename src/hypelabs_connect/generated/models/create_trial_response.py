from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class CreateTrialResponse(AdditionalDataHolder, Parsable):
    """
    Result of starting a free trial: what was provisioned and when it expires (no price, since trials are free).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # When the trial expires. Null if the trial has no expiry.
    expires_at: Optional[datetime.datetime] = None
    # Identifier of the order created for the trial.
    order_id: Optional[UUID] = None
    # Number of proxies provisioned for the trial.
    quantity: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateTrialResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateTrialResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateTrialResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "orderId": lambda n : setattr(self, 'order_id', n.get_uuid_value()),
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
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_uuid_value("orderId", self.order_id)
        writer.write_int_value("quantity", self.quantity)
        writer.write_additional_data_value(self.additional_data)
    

