from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .billing_cycles import BillingCycles
    from .order_intents import OrderIntents
    from .order_item import OrderItem
    from .order_metadata import Order_metadata
    from .order_statuses import OrderStatuses
    from .payment_methods import PaymentMethods
    from .payment_processors import PaymentProcessors

@dataclass
class Order(AdditionalDataHolder, Parsable):
    """
    An order placed by an organization, owning its lifecycle: the products it holds (its ICollection&lt;OrderItem&gt; Order.Items),its expiry and its payment link. Live status (active, grace, expired) is computed from DateTimeOffset? Order.ExpiresAtand the organization's grace policy rather than stored.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The billingCycle property
    billing_cycle: Optional[BillingCycles] = None
    # Organization's own end user the order belongs to, if any.
    customer_id: Optional[UUID] = None
    # When the order expires. Persisted so the status can be computed from it without a background worker.
    expires_at: Optional[datetime.datetime] = None
    # The caller's own reference for this order, unique within its organization when set. Makes creation    idempotent: a retry with the same reference returns this order instead of placing a duplicate.
    external_reference: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # Why the order was placed: wholesale (the organization buying for itself, on our platform account) or    retail (reselling to its own customer, on its connected account). Persisted so later actions — cancellation,    refund — resolve the same Stripe account the order settled on, instead of re-deriving it from the request.
    intent: Optional[OrderIntents] = None
    # Whether the order is still live and holding its proxies: Active, or in its post-expiry grace window.    Every other state (pending, provisioning, expired, deleted) does not.
    is_active: Optional[bool] = None
    # Recurring subscription (true) or one-shot payment (false). Does not drive expiry: it sets what the    customer is told and lets reconciliation skip one-shot orders.
    is_auto_renew: Optional[bool] = None
    # Whether the order needs attention soon: in its grace period, or expiring within a week. An    auto-renewing order is never flagged, as it renews itself rather than lapsing, and neither is a trial, which    is meant to expire.
    is_expiring_soon: Optional[bool] = None
    # Whether the order no longer holds its proxies, having handed them back to the stock for a new order:    once it is Expired or Deleted. The counterpart of bool Order.IsActive for stock; a never-provisioned order    (Pending, Provisioning) sits between the two and frees nothing.
    is_inactive: Optional[bool] = None
    # Whether the order is a trial.
    is_trial: Optional[bool] = None
    # Line items the order is made of, one per product bought. Each item carries its product, quantity and    the resources delivered for it.
    items: Optional[list[OrderItem]] = None
    # Reference of the last settlement already applied to this order, provider-prefixed (e.g.    `stripe:in_...`, `nowpayments:...`). Webhooks are delivered at least once, so a renewal that carries    this same reference has already been applied and is skipped, keeping a redelivered payment from adding a cycle    twice. Provider-agnostic so it covers every settlement source, current and future.
    last_settlement_reference: Optional[str] = None
    # The metadata property
    metadata: Optional[Order_metadata] = None
    # The paymentMethod property
    payment_method: Optional[PaymentMethods] = None
    # The paymentProcessor property
    payment_processor: Optional[PaymentProcessors] = None
    # Opaque handle at the processor (a Stripe `sub_...` or `pi_...`, a Heleket reference).
    processor_reference: Optional[str] = None
    # Total units ordered, summed over the items' quantities and not stored. Requires ICollection&lt;OrderItem&gt; Order.Items    to be loaded.
    quantity: Optional[int] = None
    # Commercial state of the order. Stored as the source of truth for states that aren't derivable from    the dates (`Provisioning`, `Expired` once a worker confirms it, and later cancellations or holds).    The transient `GracePeriod` is layered on at read time by `ResolveStatus` from DateTimeOffset? Order.ExpiresAt    and the organization's grace policy. Defaults to `Pending` (nothing paid or set up yet); each flow sets    the real state through the transition helpers.
    status: Optional[OrderStatuses] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Order:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Order
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Order()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .billing_cycles import BillingCycles
        from .order_intents import OrderIntents
        from .order_item import OrderItem
        from .order_metadata import Order_metadata
        from .order_statuses import OrderStatuses
        from .payment_methods import PaymentMethods
        from .payment_processors import PaymentProcessors

        from .billing_cycles import BillingCycles
        from .order_intents import OrderIntents
        from .order_item import OrderItem
        from .order_metadata import Order_metadata
        from .order_statuses import OrderStatuses
        from .payment_methods import PaymentMethods
        from .payment_processors import PaymentProcessors

        fields: dict[str, Callable[[Any], None]] = {
            "billingCycle": lambda n : setattr(self, 'billing_cycle', n.get_enum_value(BillingCycles)),
            "customerId": lambda n : setattr(self, 'customer_id', n.get_uuid_value()),
            "expiresAt": lambda n : setattr(self, 'expires_at', n.get_datetime_value()),
            "externalReference": lambda n : setattr(self, 'external_reference', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "intent": lambda n : setattr(self, 'intent', n.get_enum_value(OrderIntents)),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "isAutoRenew": lambda n : setattr(self, 'is_auto_renew', n.get_bool_value()),
            "isExpiringSoon": lambda n : setattr(self, 'is_expiring_soon', n.get_bool_value()),
            "isInactive": lambda n : setattr(self, 'is_inactive', n.get_bool_value()),
            "isTrial": lambda n : setattr(self, 'is_trial', n.get_bool_value()),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(OrderItem)),
            "lastSettlementReference": lambda n : setattr(self, 'last_settlement_reference', n.get_str_value()),
            "metadata": lambda n : setattr(self, 'metadata', n.get_object_value(Order_metadata)),
            "paymentMethod": lambda n : setattr(self, 'payment_method', n.get_enum_value(PaymentMethods)),
            "paymentProcessor": lambda n : setattr(self, 'payment_processor', n.get_enum_value(PaymentProcessors)),
            "processorReference": lambda n : setattr(self, 'processor_reference', n.get_str_value()),
            "quantity": lambda n : setattr(self, 'quantity', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(OrderStatuses)),
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
        writer.write_enum_value("billingCycle", self.billing_cycle)
        writer.write_uuid_value("customerId", self.customer_id)
        writer.write_datetime_value("expiresAt", self.expires_at)
        writer.write_str_value("externalReference", self.external_reference)
        writer.write_uuid_value("id", self.id)
        writer.write_enum_value("intent", self.intent)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_bool_value("isAutoRenew", self.is_auto_renew)
        writer.write_bool_value("isExpiringSoon", self.is_expiring_soon)
        writer.write_bool_value("isInactive", self.is_inactive)
        writer.write_bool_value("isTrial", self.is_trial)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_str_value("lastSettlementReference", self.last_settlement_reference)
        writer.write_object_value("metadata", self.metadata)
        writer.write_enum_value("paymentMethod", self.payment_method)
        writer.write_enum_value("paymentProcessor", self.payment_processor)
        writer.write_str_value("processorReference", self.processor_reference)
        writer.write_int_value("quantity", self.quantity)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

