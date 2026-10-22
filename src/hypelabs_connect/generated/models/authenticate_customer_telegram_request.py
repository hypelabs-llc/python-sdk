from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AuthenticateCustomerTelegramRequest(AdditionalDataHolder, Parsable):
    """
    Identity attested by Telegram after a customer started the organization's bot. The Telegram user id is trustedas-is (Telegram authenticates it; it cannot be forged), and the Connect API resolves the customer alreadylinked to it. No customer is created here: the link is established elsewhere, by a signed-in customer addingtheir Telegram account, so an unlinked user is rejected rather than silently given a fresh account.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Telegram user id (the person's `from.id`) of the account talking to the bot, as the Bot API    reports it.
    telegram_user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticateCustomerTelegramRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticateCustomerTelegramRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticateCustomerTelegramRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "telegramUserId": lambda n : setattr(self, 'telegram_user_id', n.get_str_value()),
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
        writer.write_str_value("telegramUserId", self.telegram_user_id)
        writer.write_additional_data_value(self.additional_data)
    

