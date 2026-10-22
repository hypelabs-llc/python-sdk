from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .capability_types import CapabilityTypes
    from .proxy_datacenter import ProxyDatacenter
    from .proxy_features import ProxyFeatures
    from .proxy_isp import ProxyIsp
    from .proxy_location import ProxyLocation
    from .proxy_product import ProxyProduct

@dataclass
class Proxy(AdditionalDataHolder, Parsable):
    """
    Connection details for a proxy an organization owns (one of its allocations).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The optional capabilities the proxy exposes (e.g. IPv6, IP scoring).
    capabilities: Optional[list[CapabilityTypes]] = None
    # The datacenter property
    datacenter: Optional[ProxyDatacenter] = None
    # The optional features configured on the proxy (IP rotation, ...).
    features: Optional[ProxyFeatures] = None
    # Hostname to connect to, with the reseller-facing datacenter label (e.g. `fr3.acme.com`).
    host: Optional[str] = None
    # Identifier of the proxy.
    id: Optional[UUID] = None
    # Resolved IP address.
    ip: Optional[str] = None
    # The isp property
    isp: Optional[ProxyIsp] = None
    # The location property
    location: Optional[ProxyLocation] = None
    # The organization's free-form note for this proxy, when it has annotated it.
    note: Optional[str] = None
    # Connection port.
    port: Optional[int] = None
    # The product property
    product: Optional[ProxyProduct] = None
    # The organization's tags for this proxy (empty when none).
    tags: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Proxy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Proxy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Proxy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .capability_types import CapabilityTypes
        from .proxy_datacenter import ProxyDatacenter
        from .proxy_features import ProxyFeatures
        from .proxy_isp import ProxyIsp
        from .proxy_location import ProxyLocation
        from .proxy_product import ProxyProduct

        from .capability_types import CapabilityTypes
        from .proxy_datacenter import ProxyDatacenter
        from .proxy_features import ProxyFeatures
        from .proxy_isp import ProxyIsp
        from .proxy_location import ProxyLocation
        from .proxy_product import ProxyProduct

        fields: dict[str, Callable[[Any], None]] = {
            "capabilities": lambda n : setattr(self, 'capabilities', n.get_collection_of_enum_values(CapabilityTypes)),
            "datacenter": lambda n : setattr(self, 'datacenter', n.get_object_value(ProxyDatacenter)),
            "features": lambda n : setattr(self, 'features', n.get_object_value(ProxyFeatures)),
            "host": lambda n : setattr(self, 'host', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "isp": lambda n : setattr(self, 'isp', n.get_object_value(ProxyIsp)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(ProxyLocation)),
            "note": lambda n : setattr(self, 'note', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "product": lambda n : setattr(self, 'product', n.get_object_value(ProxyProduct)),
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
        writer.write_collection_of_enum_values("capabilities", self.capabilities)
        writer.write_object_value("datacenter", self.datacenter)
        writer.write_object_value("features", self.features)
        writer.write_str_value("host", self.host)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("ip", self.ip)
        writer.write_object_value("isp", self.isp)
        writer.write_object_value("location", self.location)
        writer.write_str_value("note", self.note)
        writer.write_int_value("port", self.port)
        writer.write_object_value("product", self.product)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_additional_data_value(self.additional_data)
    

