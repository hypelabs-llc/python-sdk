from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ProxyIpRotationFeature(AdditionalDataHolder, Parsable):
    """
    An active IP-rotation schedule on a proxy.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Rotation interval in whole minutes.
    interval_minutes: Optional[int] = None
    # Rotation interval in whole seconds.
    interval_seconds: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProxyIpRotationFeature:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxyIpRotationFeature
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProxyIpRotationFeature()
    
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
    

