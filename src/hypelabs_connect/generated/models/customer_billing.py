from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerBilling(AdditionalDataHolder, Parsable):
    """
    Legal billing address and tax identifiers shown on a customer's invoices. Value object owned byCustomer with no identity of its own; all fields are optional.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Street address (line 1).
    address_line: Optional[str] = None
    # City.
    city: Optional[str] = None
    # The company's legal name, when bool CustomerBilling.IsCompany is true.
    company_name: Optional[str] = None
    # Country (ISO 3166-1 alpha-2 code or name).
    country: Optional[str] = None
    # Whether the customer is billed as a company (B2B) rather than an individual (B2C). When true,    string? CustomerBilling.CompanyName and string? CustomerBilling.TaxId apply.
    is_company: Optional[bool] = None
    # Postal / ZIP code.
    postal_code: Optional[str] = None
    # Company registration number (e.g. SIREN/SIRET, Companies House number), distinct from the VAT/tax    number in string? CustomerBilling.TaxId. Applies when bool CustomerBilling.IsCompany is true.
    registration_number: Optional[str] = None
    # VAT / tax identification number.
    tax_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerBilling:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerBilling
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerBilling()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "addressLine": lambda n : setattr(self, 'address_line', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "isCompany": lambda n : setattr(self, 'is_company', n.get_bool_value()),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "registrationNumber": lambda n : setattr(self, 'registration_number', n.get_str_value()),
            "taxId": lambda n : setattr(self, 'tax_id', n.get_str_value()),
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
        writer.write_str_value("addressLine", self.address_line)
        writer.write_str_value("city", self.city)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("country", self.country)
        writer.write_bool_value("isCompany", self.is_company)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("registrationNumber", self.registration_number)
        writer.write_str_value("taxId", self.tax_id)
        writer.write_additional_data_value(self.additional_data)
    

