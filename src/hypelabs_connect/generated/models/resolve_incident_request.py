from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ResolveIncidentRequest(AdditionalDataHolder, Parsable):
    """
    Payload to resolve an open incident on a target.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Predefined reason the target went down.
    reason: Optional[str] = None
    # Note for the customer, stored on the incident and shown to them later. Null when no note is provided.
    resolution_note: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ResolveIncidentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ResolveIncidentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ResolveIncidentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "resolutionNote": lambda n : setattr(self, 'resolution_note', n.get_str_value()),
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
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("resolutionNote", self.resolution_note)
        writer.write_additional_data_value(self.additional_data)
    

