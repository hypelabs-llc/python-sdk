from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class CustomerAuthResponse(AdditionalDataHolder, Parsable):
    """
    The result of a successful customer sign-in (password or OAuth): the inherited bearer token and expiry,    plus the identity the front-end needs.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # JWT bearer token to send in the Authorization header.
    access_token: Optional[str] = None
    # The customer's avatar URL (their Gravatar, falling back to a neutral silhouette).
    avatar: Optional[str] = None
    # The customer's email address.
    email: Optional[str] = None
    # Instant the access token stops being valid.
    expires_at: Optional[datetime.datetime] = None
    # Whether the customer is banned (suspended). False for an active account.
    is_banned: Optional[bool] = None
    # The customer's preferred locale (e.g. `en-US`), when set.
    locale: Optional[str] = None
    # The customer's display name, when set.
    name: Optional[str] = None
    # The customer's unique identifier.
    user_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerAuthResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerAuthResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerAuthResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "accessToken": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "avatar": lambda n : setattr(self, 'avatar', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "isBanned": lambda n : setattr(self, 'is_banned', n.get_bool_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_uuid_value()),
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
        writer.write_str_value("accessToken", self.access_token)
        writer.write_str_value("avatar", self.avatar)
        writer.write_str_value("email", self.email)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_bool_value("isBanned", self.is_banned)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("name", self.name)
        writer.write_uuid_value("userId", self.user_id)
        writer.write_additional_data_value(self.additional_data)
    

