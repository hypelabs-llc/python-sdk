from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CustomerKyc(AdditionalDataHolder, Parsable):
    """
    Know-your-customer details a customer submits before their first order: intended proxy usage, acceptable-usepolicy acknowledgement, and the submitted/approved state. Stored as JSON on the Customer.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Whether the submitted KYC has been approved by HypeLabs.
    approved: Optional[bool] = None
    # Free-text description of how the customer intends to use the proxies.
    description: Optional[str] = None
    # Whether the customer acknowledged the acceptable-use policy when submitting.
    policy_acknowledged: Optional[bool] = None
    # Domain area the customer selected for their proxy usage (e.g. "ad-verification", "seo").
    scope_of_use: Optional[str] = None
    # Whether the customer has submitted their KYC details.
    submitted: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomerKyc:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomerKyc
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomerKyc()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "approved": lambda n : setattr(self, 'approved', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "policyAcknowledged": lambda n : setattr(self, 'policy_acknowledged', n.get_bool_value()),
            "scopeOfUse": lambda n : setattr(self, 'scope_of_use', n.get_str_value()),
            "submitted": lambda n : setattr(self, 'submitted', n.get_bool_value()),
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
        writer.write_bool_value("approved", self.approved)
        writer.write_str_value("description", self.description)
        writer.write_bool_value("policyAcknowledged", self.policy_acknowledged)
        writer.write_str_value("scopeOfUse", self.scope_of_use)
        writer.write_bool_value("submitted", self.submitted)
        writer.write_additional_data_value(self.additional_data)
    

