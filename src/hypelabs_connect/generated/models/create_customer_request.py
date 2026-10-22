from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .customer_billing import CustomerBilling

@dataclass
class CreateCustomerRequest(AdditionalDataHolder, Parsable):
    """
    Payload to create a customer (your organization's own end user).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billing property
    billing: Optional[CustomerBilling] = None
    # Name shown for the customer in the dashboard and emails.
    display_name: Optional[str] = None
    # Email address of the customer. Must be unique within your organization.
    email: Optional[str] = None
    # Identifier of the customer in your own system. Matches records across systems and makes creation idempotent.
    external_id: Optional[str] = None
    # Preferred locale (e.g. "en", "fr") for emails and OTP messages.
    locale: Optional[str] = None
    # Initial password of the customer, stored hashed. Omit for an OAuth-only or passwordless user.
    password: Optional[str] = None
    # Phone number of the customer.
    phone_number: Optional[str] = None
    # Page (your own) linked in the verification email sent on creation, with the token appended as a query parameter. Omit to leave the email unverified and skip the email.
    verification_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateCustomerRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateCustomerRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateCustomerRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .customer_billing import CustomerBilling

        from .customer_billing import CustomerBilling

        fields: dict[str, Callable[[Any], None]] = {
            "billing": lambda n : setattr(self, 'billing', n.get_object_value(CustomerBilling)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "verificationUrl": lambda n : setattr(self, 'verification_url', n.get_str_value()),
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
        writer.write_object_value("billing", self.billing)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("externalId", self.external_id)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("password", self.password)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("verificationUrl", self.verification_url)
        writer.write_additional_data_value(self.additional_data)
    

