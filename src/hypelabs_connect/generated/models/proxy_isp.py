from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class ProxyIsp(AdditionalDataHolder, Parsable):
    """
    A proxy's ISP.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Identifier of the ISP, to refetch or reorder it.
    id: Optional[UUID] = None
    # Logo URL of the ISP, when known.
    logo_url: Optional[str] = None
    # Name of the ISP, when known.
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProxyIsp:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxyIsp
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProxyIsp()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "logoUrl": lambda n : setattr(self, 'logo_url', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("logoUrl", self.logo_url)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

