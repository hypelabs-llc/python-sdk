from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class IpRotationLinkResponse(AdditionalDataHolder, Parsable):
    """
    A self-contained IP rotation link for a proxy: the raw token plus the ready-to-use link.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The IP rotation link served on the organization's IP rotation domain (its own, or the default).
    link: Optional[str] = None
    # The IP rotation token (a protected customer id). Use it to build your own link if needed.
    token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpRotationLinkResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpRotationLinkResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpRotationLinkResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_str_value("link", self.link)
        writer.write_str_value("token", self.token)
        writer.write_additional_data_value(self.additional_data)
    

