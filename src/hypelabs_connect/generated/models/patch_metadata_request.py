from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .patch_metadata_request_metadata import PatchMetadataRequest_metadata

@dataclass
class PatchMetadataRequest(AdditionalDataHolder, Parsable):
    """
    Merge-patch of an entity's metadata (RFC 7386 semantics): a present key sets or overwrites its value,    a null value removes the key, and any key not listed is left unchanged.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Metadata keys to merge: a non-null value is written (overwriting any existing one) and a null value removes the key.
    metadata: Optional[PatchMetadataRequest_metadata] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PatchMetadataRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PatchMetadataRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PatchMetadataRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .patch_metadata_request_metadata import PatchMetadataRequest_metadata

        from .patch_metadata_request_metadata import PatchMetadataRequest_metadata

        fields: dict[str, Callable[[Any], None]] = {
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(PatchMetadataRequest_metadata)),
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
        writer.write_object_value("metadata", self.metadata)
        writer.write_additional_data_value(self.additional_data)
    

