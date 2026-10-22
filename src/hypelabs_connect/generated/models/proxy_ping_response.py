from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ProxyPingResponse(AdditionalDataHolder, Parsable):
    """
    The result of testing a proxy through a real request: whether it answered, the round-trip latency,    the HTTP status the request came back with, and the exit IP the proxy routed through.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The public IP the proxy routed the request through, as reported by the reach target; null when    unreachable or the target didn't return one.
    exit_ip: Optional[str] = None
    # Round-trip latency in milliseconds when reachable; null otherwise.
    latency_milliseconds: Optional[int] = None
    # Whether the proxy answered the request.
    reachable: Optional[bool] = None
    # The HTTP status code the request came back with; null when the proxy couldn't be reached.
    status_code: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProxyPingResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxyPingResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProxyPingResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "exitIp": lambda n : setattr(self, 'exit_ip', n.get_str_value()),
            "latencyMilliseconds": lambda n : setattr(self, 'latency_milliseconds', n.get_int_value()),
            "reachable": lambda n : setattr(self, 'reachable', n.get_bool_value()),
            "statusCode": lambda n : setattr(self, 'status_code', n.get_int_value()),
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
        writer.write_str_value("exitIp", self.exit_ip)
        writer.write_int_value("latencyMilliseconds", self.latency_milliseconds)
        writer.write_bool_value("reachable", self.reachable)
        writer.write_int_value("statusCode", self.status_code)
        writer.write_additional_data_value(self.additional_data)
    

