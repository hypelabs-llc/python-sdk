from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class ProxyLocation(AdditionalDataHolder, Parsable):
    """
    Where a proxy is located.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # City, when known.
    city: Optional[str] = None
    # ISO 3166-1 alpha-2 country code (e.g. `FR`), when known.
    country_code: Optional[str] = None
    # Identifier of the location, to refetch or reorder it.
    id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ProxyLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ProxyLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ProxyLocation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
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
        writer.write_str_value("city", self.city)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_uuid_value("id", self.id)
        writer.write_additional_data_value(self.additional_data)
    

