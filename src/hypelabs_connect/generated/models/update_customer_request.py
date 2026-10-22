from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .customer_billing import CustomerBilling
    from .update_customer_request_external_logins import UpdateCustomerRequest_externalLogins

@dataclass
class UpdateCustomerRequest(AdditionalDataHolder, Parsable):
    """
    Payload to update a customer. Null fields are left unchanged.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billing property
    billing: Optional[CustomerBilling] = None
    # New display name. Null leaves it unchanged.
    display_name: Optional[str] = None
    # New email. Null leaves it unchanged.
    email: Optional[str] = None
    # New external id. Null leaves it unchanged.
    external_id: Optional[str] = None
    # Replacement external logins (OAuth provider -&gt; subject). Null leaves them unchanged.
    external_logins: Optional[UpdateCustomerRequest_externalLogins] = None
    # New locale (BCP-47 tag). Null leaves it unchanged.
    locale: Optional[str] = None
    # New phone number. Null leaves it unchanged.
    phone_number: Optional[str] = None
    # New push-notifications token. Null leaves it unchanged.
    push_notifications_token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateCustomerRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateCustomerRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateCustomerRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .customer_billing import CustomerBilling
        from .update_customer_request_external_logins import UpdateCustomerRequest_externalLogins

        from .customer_billing import CustomerBilling
        from .update_customer_request_external_logins import UpdateCustomerRequest_externalLogins

        fields: dict[str, Callable[[Any], None]] = {
            "billing": lambda n : setattr(self, 'billing', n.get_object_value(CustomerBilling)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "externalLogins": lambda n : setattr(self, 'external_logins', n.get_object_value(UpdateCustomerRequest_externalLogins)),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
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
        writer.write_object_value("billing", self.billing)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("externalLogins", self.external_logins)
        writer.write_str_value("locale", self.locale)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("pushNotificationsToken", self.push_notifications_token)
        writer.write_additional_data_value(self.additional_data)
    

