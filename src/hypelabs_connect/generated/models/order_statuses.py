from enum import Enum

class OrderStatuses(str, Enum):
    Pending = "Pending",
    Provisioning = "Provisioning",
    Active = "Active",
    GracePeriod = "GracePeriod",
    Expired = "Expired",
    Deleted = "Deleted",

