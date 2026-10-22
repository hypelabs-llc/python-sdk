from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AuthenticateCustomerOAuthRequest(AdditionalDataHolder, Parsable):
    """
    Identity attested by an external provider (Google, GitHub, Apple, ...) after the organization's own front-end(or app) completed the OAuth sign-in. The Connect API trusts the attested identity — it never talks to theprovider itself — and finds or creates the matching customer, scoped to the calling organization.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Display name reported by the provider, used when creating the customer. Null when the provider gives none.
    display_name: Optional[str] = None
    # Email address attested by the provider, used to link the sign-in to an existing customer or create one.    Optional: Apple only returns it on the first authorization, so later sign-ins match by the provider link alone.    Required when no customer matches yet (a first-time sign-in with no email cannot create an account).
    email: Optional[str] = None
    # Preferred locale (e.g. `en-US`) reported by the provider. Refreshed on each sign-in; ignored when null.
    locale: Optional[str] = None
    # Provider key the customer signed in through, e.g. `google`, `apple`, `discord`. A free    string, not an enum: an organization can wire up any provider without Connect needing a new release.
    provider: Optional[str] = None
    # Stable identifier of the customer at the provider (the provider's account id).
    provider_id: Optional[str] = None
    # Device push-notification token (e.g. the app's APNs token), sent at sign-in. Refreshed when provided;    ignored when null.
    push_notifications_token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticateCustomerOAuthRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticateCustomerOAuthRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticateCustomerOAuthRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "providerId": lambda n : setattr(self, 'provider_id', n.get_str_value()),
            "pushNotificationsToken": lambda n : setattr(self, 'push_notifications_token', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("providerId", self.provider_id)
        writer.write_str_value("pushNotificationsToken", self.push_notifications_token)
        writer.write_additional_data_value(self.additional_data)
    

