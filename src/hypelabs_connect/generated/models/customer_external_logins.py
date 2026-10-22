from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Customer_externalLogins(AdditionalDataHolder, Parsable):
    """
    The user's external OAuth logins, keyed by provider (e.g. "apple", "google") with the provider's    user identifier as the value. Stored as JSON. Null when the user has no linked social logins.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Customer_externalLogins:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Customer_externalLogins
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Customer_externalLogins()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
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
        writer.write_additional_data_value(self.additional_data)
    

