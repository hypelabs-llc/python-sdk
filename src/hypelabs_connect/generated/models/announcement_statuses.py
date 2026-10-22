from enum import Enum

class AnnouncementStatuses(str, Enum):
    Draft = "Draft",
    Published = "Published",
    Archived = "Archived",

