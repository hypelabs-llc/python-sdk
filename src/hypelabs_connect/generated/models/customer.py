from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .customer_billing import CustomerBilling
    from .customer_external_logins import Customer_externalLogins
    from .customer_kyc import CustomerKyc
    from .customer_metadata import Customer_metadata
    from .grace_period_policies import GracePeriodPolicies
    from .password_hash_schemes import PasswordHashSchemes

@dataclass
class Customer(AdditionalDataHolder, Parsable):
    """
    An end user that an Organization? Customer.Organization manages through its API, scoped to that organization so twoorgs can hold the same email without collision. Not an ASP.NET Identity user (that is the platform's ownUser): customers never enter the auth pipeline.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Domains the customer's proxies authorize by default. Empty means no domain restriction set here;    `*` allows all.
    allowed_domains: Optional[list[str]] = None
    # IP addresses the customer's proxies authorize by default. Empty means no IP restriction set here.
    allowed_ips: Optional[list[str]] = None
    # The user's Gravatar avatar URL, derived from their email (falls back to a neutral silhouette    when the address has no Gravatar). Computed, not stored.
    avatar_url: Optional[str] = None
    # When the customer was banned. Null while active: banning disables access without deleting the    record, so the value is kept for the audit trail.
    banned_at: Optional[datetime.datetime] = None
    # The billing property
    billing: Optional[CustomerBilling] = None
    # The customer's ISO 3166-1 alpha-2 country code (uppercase): their billing country when set,    otherwise the region of their locale (e.g. `en-US` → `US`). Computed, not persisted.
    country_code: Optional[str] = None
    # Display name shown for the customer. Null when none was provided.
    display_name: Optional[str] = None
    # The customer's email. Unique within the owning organization.
    email: Optional[str] = None
    # Whether the email has been verified, set true when the customer follows the verification link    (see `CustomerService.VerifyEmailAsync`). Defaults to false.
    email_verified: Optional[bool] = None
    # Identifier this customer has in the organization's own system, matched to keep creation    idempotent. Null when the organization supplies none.
    external_id: Optional[str] = None
    # The user's external OAuth logins, keyed by provider (e.g. "apple", "google") with the provider's    user identifier as the value. Stored as JSON. Null when the user has no linked social logins.
    external_logins: Optional[Customer_externalLogins] = None
    # The gracePeriodPolicy property
    grace_period_policy: Optional[GracePeriodPolicies] = None
    # The id property
    id: Optional[UUID] = None
    # Whether the user is allowed to authenticate. False = banned; set DateTimeOffset? Customer.BannedAt too.    Defaults to true.
    is_active: Optional[bool] = None
    # Whether this customer is a company (B2B) rather than an individual. True only when billing says so;    a customer with no billing is treated as an individual. Computed, not persisted — the `isCompany` query    filter runs on this in memory, so a missing billing correctly counts as a person.
    is_company: Optional[bool] = None
    # The kyc property
    kyc: Optional[CustomerKyc] = None
    # When the user last signed in, if ever. Null until their first login.
    last_login_at: Optional[datetime.datetime] = None
    # The user's preferred locale (e.g. "en", "fr") for localized emails and OTP messages. Null until set.
    locale: Optional[str] = None
    # The metadata property
    metadata: Optional[Customer_metadata] = None
    # Scheme that produced string? Customer.PasswordHash, defaulting to BCrypt. A Legacy hash is an import    from a previous system, verified as-is and upgraded to BCrypt on the next successful login. The scheme is    exposed to clients (the admin surface shows it) even though the hash itself never is.
    password_hash_scheme: Optional[PasswordHashSchemes] = None
    # The user's id with the payment processor (e.g. a Stripe customer id), if one has been created    for them. Generic across processors; null until set.
    payment_customer_id: Optional[str] = None
    # The user's phone number, if provided. Null until set.
    phone_number: Optional[str] = None
    # The device token used to send this user push notifications, if one has been registered. Null    until set.
    push_notifications_token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Customer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Customer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Customer()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .customer_billing import CustomerBilling
        from .customer_external_logins import Customer_externalLogins
        from .customer_kyc import CustomerKyc
        from .customer_metadata import Customer_metadata
        from .grace_period_policies import GracePeriodPolicies
        from .password_hash_schemes import PasswordHashSchemes

        from .customer_billing import CustomerBilling
        from .customer_external_logins import Customer_externalLogins
        from .customer_kyc import CustomerKyc
        from .customer_metadata import Customer_metadata
        from .grace_period_policies import GracePeriodPolicies
        from .password_hash_schemes import PasswordHashSchemes

        fields: dict[str, Callable[[Any], None]] = {
            "allowedDomains": lambda n : setattr(self, 'allowed_domains', n.get_collection_of_primitive_values(str)),
            "allowedIps": lambda n : setattr(self, 'allowed_ips', n.get_collection_of_primitive_values(str)),
            "avatarUrl": lambda n : setattr(self, 'avatar_url', n.get_str_value()),
            "bannedAt": lambda n : setattr(self, 'banned_at', n.get_datetime_value()),
            "billing": lambda n : setattr(self, 'billing', n.get_object_value(CustomerBilling)),
            "countryCode": lambda n : setattr(self, 'country_code', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "emailVerified": lambda n : setattr(self, 'email_verified', n.get_bool_value()),
            "externalId": lambda n : setattr(self, 'external_id', n.get_str_value()),
            "externalLogins": lambda n : setattr(self, 'external_logins', n.get_object_value(Customer_externalLogins)),
            "gracePeriodPolicy": lambda n : setattr(self, 'grace_period_policy', n.get_enum_value(GracePeriodPolicies)),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "isCompany": lambda n : setattr(self, 'is_company', n.get_bool_value()),
            "kyc": lambda n : setattr(self, 'kyc', n.get_object_value(CustomerKyc)),
            "lastLoginAt": lambda n : setattr(self, 'last_login_at', n.get_datetime_value()),
            "locale": lambda n : setattr(self, 'locale', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(Customer_metadata)),
            "passwordHashScheme": lambda n : setattr(self, 'password_hash_scheme', n.get_enum_value(PasswordHashSchemes)),
            "paymentCustomerId": lambda n : setattr(self, 'payment_customer_id', n.get_str_value()),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "pushNotificationsToken": lambda n : setattr(self, 'push_notifications_token', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("allowedDomains", self.allowed_domains)
        writer.write_collection_of_primitive_values("allowedIps", self.allowed_ips)
        writer.write_str_value("avatarUrl", self.avatar_url)
        writer.write_datetime_value("bannedAt", self.banned_at)
        writer.write_object_value("billing", self.billing)
        writer.write_str_value("countryCode", self.country_code)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_bool_value("emailVerified", self.email_verified)
        writer.write_str_value("externalId", self.external_id)
        writer.write_object_value("externalLogins", self.external_logins)
        writer.write_enum_value("gracePeriodPolicy", self.grace_period_policy)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_bool_value("isCompany", self.is_company)
        writer.write_object_value("kyc", self.kyc)
        writer.write_datetime_value("lastLoginAt", self.last_login_at)
        writer.write_str_value("locale", self.locale)
        writer.write_object_value("metadata", self.metadata)
        writer.write_enum_value("passwordHashScheme", self.password_hash_scheme)
        writer.write_str_value("paymentCustomerId", self.payment_customer_id)
        writer.write_str_value("phoneNumber", self.phone_number)
        writer.write_str_value("pushNotificationsToken", self.push_notifications_token)
        writer.write_additional_data_value(self.additional_data)
    

