from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ProxyIpRotationResponse(AdditionalDataHolder, Parsable):
    """
    The IP rotation configured on a proxy: how often its IP rotates, in seconds and whole minutes. Fetched livefrom the Manager; a 404 means no rotation is configured.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Interval between IP rotations, in whole minutes.
    interval_minutes: Optional[int] = None
    # Interval between IP rotations, in seconds.
    interval_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProxyIpRotationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxyIpRotationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProxyIpRotationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "intervalMinutes": lambda n : setattr(self, 'interval_minutes', n.get_int_value()),
            "intervalSeconds": lambda n : setattr(self, 'interval_seconds', n.get_int_value()),
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
        writer.write_int_value("intervalMinutes", self.interval_minutes)
        writer.write_int_value("intervalSeconds", self.interval_seconds)
        writer.write_additional_data_value(self.additional_data)
    

