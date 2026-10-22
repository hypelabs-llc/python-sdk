from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UpdateProxyCredentialsRequest(AdditionalDataHolder, Parsable):
    """
    Request to change an allocated proxy's credentials. A null username or password is generated from the    organization's default formats.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # IP addresses allowed to use the proxy.
    allowed_ips: Optional[list[str]] = None
    # New authentication password. Generated from the organization's default format when null.
    password: Optional[str] = None
    # New authentication username. Generated from the organization's default format when null.
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateProxyCredentialsRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateProxyCredentialsRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateProxyCredentialsRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowedIps": lambda n : setattr(self, 'allowed_ips', n.get_collection_of_primitive_values(str)),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "username": lambda n : setattr(self, 'username', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("allowedIps", self.allowed_ips)
        writer.write_str_value("password", self.password)
        writer.write_str_value("username", self.username)
        writer.write_additional_data_value(self.additional_data)
    

