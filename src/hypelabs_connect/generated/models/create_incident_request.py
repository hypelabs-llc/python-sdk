from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CreateIncidentRequest(AdditionalDataHolder, Parsable):
    """
    Payload to open a new incident.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Free-form details about the incident.
    description: Optional[str] = None
    # Email address of the person reporting the incident.
    reporter_email: Optional[str] = None
    # Short title summarizing the incident.
    subject: Optional[str] = None
    # Identifier of the affected resource.
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateIncidentRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateIncidentRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateIncidentRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "reporterEmail": lambda n : setattr(self, 'reporter_email', n.get_str_value()),
            "subject": lambda n : setattr(self, 'subject', n.get_str_value()),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_str_value("reporterEmail", self.reporter_email)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

