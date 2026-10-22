from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .announcement_metadata import Announcement_metadata
    from .announcement_statuses import AnnouncementStatuses

@dataclass
class Announcement(AdditionalDataHolder, Parsable):
    """
    A promotional card shown to organizations in the dashboard: a headline with an optional image, body and link.Only AnnouncementStatuses.Published ones are shown, most recent first.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Body text of the announcement, shown under the title.
    body: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # URL of the image displayed on the card.
    image_url: Optional[str] = None
    # True when the announcement is published and currently visible.
    is_live: Optional[bool] = None
    # Label of the link's call-to-action button (e.g. "Learn more").
    link_label: Optional[str] = None
    # Destination URL opened when the card is clicked.
    link_url: Optional[str] = None
    # The metadata property
    metadata: Optional[Announcement_metadata] = None
    # Publication state of the announcement: only Published ones are shown.
    status: Optional[AnnouncementStatuses] = None
    # Headline displayed at the top of the card.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Announcement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Announcement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Announcement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .announcement_metadata import Announcement_metadata
        from .announcement_statuses import AnnouncementStatuses

        from .announcement_metadata import Announcement_metadata
        from .announcement_statuses import AnnouncementStatuses

        fields: dict[str, Callable[[Any], None]] = {
            "body": lambda n : setattr(self, 'body', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "imageUrl": lambda n : setattr(self, 'image_url', n.get_str_value()),
            "isLive": lambda n : setattr(self, 'is_live', n.get_bool_value()),
            "linkLabel": lambda n : setattr(self, 'link_label', n.get_str_value()),
            "linkUrl": lambda n : setattr(self, 'link_url', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(Announcement_metadata)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(AnnouncementStatuses)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("body", self.body)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("imageUrl", self.image_url)
        writer.write_bool_value("isLive", self.is_live)
        writer.write_str_value("linkLabel", self.link_label)
        writer.write_str_value("linkUrl", self.link_url)
        writer.write_object_value("metadata", self.metadata)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

