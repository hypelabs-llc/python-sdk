from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ProxyCredentialResponse(AdditionalDataHolder, Parsable):
    """
    The credentials in effect on a proxy: the username and password to authenticate with, the IPs and domainsallowed to use it, and when they were applied. Stored in and read from Vault.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Domains the proxy is permitted to reach. Empty when no domain allowlist applies.
    allowed_domains: Optional[list[str]] = None
    # IP addresses allowed to connect through the proxy. Empty when access is not restricted by IP.
    allowed_ips: Optional[list[str]] = None
    # Instant these credentials were applied to the proxy in Vault.
    applied_at: Optional[datetime.datetime] = None
    # Password used to authenticate against the proxy. Null when no credentials are stored yet.
    password: Optional[str] = None
    # Username used to authenticate against the proxy. Null when no credentials are stored yet.
    username: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProxyCredentialResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxyCredentialResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProxyCredentialResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "allowedDomains": lambda n : setattr(self, 'allowed_domains', n.get_collection_of_primitive_values(str)),
            "allowedIps": lambda n : setattr(self, 'allowed_ips', n.get_collection_of_primitive_values(str)),
            "appliedAt": lambda n : setattr(self, 'applied_at', n.get_datetime_value()),
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
        writer.write_collection_of_primitive_values("allowedDomains", self.allowed_domains)
        writer.write_collection_of_primitive_values("allowedIps", self.allowed_ips)
        writer.write_datetime_value("appliedAt", self.applied_at)
        writer.write_str_value("password", self.password)
        writer.write_str_value("username", self.username)
        writer.write_additional_data_value(self.additional_data)
    

