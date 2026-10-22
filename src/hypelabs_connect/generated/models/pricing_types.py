from enum import Enum

class PricingTypes(str, Enum):
    PerUnit = "PerUnit",
    PerBandwidth = "PerBandwidth",

