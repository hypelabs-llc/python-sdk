from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .proxy_options_metadata import ProxyOptions_metadata
    from .resolution_modes import ResolutionModes

@dataclass
class ProxyOptions(AdditionalDataHolder, Parsable):
    """
    Feature options for an inventory proxy: settings toggled on the proxy, such as the resolution mode. There is noproxy table (proxies live in the Manager), so this references the proxy by id only; at most one options row perproxy. Options that need a capability are only valid on a proxy exposing it.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The id property
    id: Optional[UUID] = None
    # The metadata property
    metadata: Optional[ProxyOptions_metadata] = None
    # The inventory proxy these options are about. No foreign key: proxies aren't stored locally.
    proxy_id: Optional[UUID] = None
    # How the proxy resolves addresses. The non-default modes need the proxy's IPv6 capability.
    resolution_mode: Optional[ResolutionModes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProxyOptions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxyOptions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProxyOptions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .proxy_options_metadata import ProxyOptions_metadata
        from .resolution_modes import ResolutionModes

        from .proxy_options_metadata import ProxyOptions_metadata
        from .resolution_modes import ResolutionModes

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(ProxyOptions_metadata)),
            "proxyId": lambda n : setattr(self, 'proxy_id', n.get_uuid_value()),
            "resolutionMode": lambda n : setattr(self, 'resolution_mode', n.get_enum_value(ResolutionModes)),
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
        writer.write_object_value("metadata", self.metadata)
        writer.write_uuid_value("proxyId", self.proxy_id)
        writer.write_enum_value("resolutionMode", self.resolution_mode)
        writer.write_additional_data_value(self.additional_data)
    

