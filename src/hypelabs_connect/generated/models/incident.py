from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .incident_metadata import Incident_metadata
    from .incident_statuses import IncidentStatuses

@dataclass
class Incident(AdditionalDataHolder, Parsable):
    """
    A complaint reported about a proxy (or other resource), usually by a customer. string Incident.Target andstring Incident.ReporterEmail are free-form strings until they are linked to their own entities.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Full text of the complaint, null when none was provided.
    description: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # True when the incident is still open and was created more than TimeSpan Incident.DefaultOverdueAfter ago.
    is_overdue: Optional[bool] = None
    # The metadata property
    metadata: Optional[Incident_metadata] = None
    # Why the target went down, picked from the predefined reasons when the incident is resolved.
    reason: Optional[str] = None
    # Email of the customer who reported the incident.
    reporter_email: Optional[str] = None
    # Message written for the customer at resolution, surfaced to them (e.g. by email) later.
    resolution_note: Optional[str] = None
    # When the incident was resolved, null while it is still open.
    resolved_at: Optional[datetime.datetime] = None
    # Lifecycle state of the incident (open, resolved, etc.).
    status: Optional[IncidentStatuses] = None
    # Short one-line title of the complaint.
    subject: Optional[str] = None
    # Identifier of the affected proxy (hostname:port).
    target: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Incident:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Incident
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Incident()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .incident_metadata import Incident_metadata
        from .incident_statuses import IncidentStatuses

        from .incident_metadata import Incident_metadata
        from .incident_statuses import IncidentStatuses

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isOverdue": lambda n : setattr(self, 'is_overdue', n.get_bool_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(Incident_metadata)),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "reporterEmail": lambda n : setattr(self, 'reporter_email', n.get_str_value()),
            "resolutionNote": lambda n : setattr(self, 'resolution_note', n.get_str_value()),
            "resolvedAt": lambda n : setattr(self, 'resolved_at', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(IncidentStatuses)),
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
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isOverdue", self.is_overdue)
        writer.write_object_value("metadata", self.metadata)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("reporterEmail", self.reporter_email)
        writer.write_str_value("resolutionNote", self.resolution_note)
        writer.write_datetime_value("resolvedAt", self.resolved_at)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("subject", self.subject)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    

