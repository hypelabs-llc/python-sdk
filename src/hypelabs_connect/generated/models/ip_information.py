from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class IpInformation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The asn property
    asn: Optional[str] = None
    # The asnDomain property
    asn_domain: Optional[str] = None
    # The asnLogo property
    asn_logo: Optional[str] = None
    # The continent property
    continent: Optional[str] = None
    # The continentCode property
    continent_code: Optional[str] = None
    # The country property
    country: Optional[str] = None
    # The countryCode property
    country_code: Optional[str] = None
    # The countryFlag property
    country_flag: Optional[str] = None
    # The countryFlagUrl property
    country_flag_url: Optional[str] = None
    # The currencyCode property
    currency_code: Optional[str] = None
    # The currencySymbol property
    currency_symbol: Optional[str] = None
    # The ipAddress property
    ip_address: Optional[str] = None
    # The isAnycast property
    is_anycast: Optional[bool] = None
    # The isp property
    isp: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpInformation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpInformation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpInformation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "asn": lambda n : setattr(self, 'asn', n.get_str_value()),
            "asnDomain": lambda n : setattr(self, 'asn_domain', n.get_str_value()),
            "asnLogo": lambda n : setattr(self, 'asn_logo', n.get_str_value()),
            "continent": lambda n : setattr(self, 'continent', n.get_str_value()),
            "continentCode": lambda n : setattr(self, 'continent_code', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "countryFlag": lambda n : setattr(self, 'country_flag', n.get_str_value()),
            "countryFlagUrl": lambda n : setattr(self, 'country_flag_url', n.get_str_value()),
            "currencyCode": lambda n : setattr(self, 'currency_code', n.get_str_value()),
            "currencySymbol": lambda n : setattr(self, 'currency_symbol', n.get_str_value()),
            "ipAddress": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "isAnycast": lambda n : setattr(self, 'is_anycast', n.get_bool_value()),
            "isp": lambda n : setattr(self, 'isp', n.get_str_value()),
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
        writer.write_str_value("asn", self.asn)
        writer.write_str_value("asnDomain", self.asn_domain)
        writer.write_str_value("asnLogo", self.asn_logo)
        writer.write_str_value("continent", self.continent)
        writer.write_str_value("continentCode", self.continent_code)
        writer.write_str_value("country", self.country)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_str_value("countryFlag", self.country_flag)
        writer.write_str_value("countryFlagUrl", self.country_flag_url)
        writer.write_str_value("currencyCode", self.currency_code)
        writer.write_str_value("currencySymbol", self.currency_symbol)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_bool_value("isAnycast", self.is_anycast)
        writer.write_str_value("isp", self.isp)
        writer.write_additional_data_value(self.additional_data)
    

