from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PatchProxyAnnotationRequest(AdditionalDataHolder, Parsable):
    """
    Patch of an organization's annotation of a proxy: its free-form note and its tags. A null field is    left unchanged; an empty string clears the note and an empty array clears the tags.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The free-form note. Null leaves it unchanged; an empty string clears it.
    note: Optional[str] = None
    # The tags. Null leaves them unchanged; an empty array clears them.
    tags: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PatchProxyAnnotationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PatchProxyAnnotationRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PatchProxyAnnotationRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("note", self.note)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_additional_data_value(self.additional_data)
    

