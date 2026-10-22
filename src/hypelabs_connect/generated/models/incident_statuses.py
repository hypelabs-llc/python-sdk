from enum import Enum

class IncidentStatuses(str, Enum):
    Open = "Open",
    Resolved = "Resolved",
    Dismissed = "Dismissed",

