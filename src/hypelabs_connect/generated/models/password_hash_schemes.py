from enum import Enum

class PasswordHashSchemes(str, Enum):
    Bcrypt = "Bcrypt",
    Legacy = "Legacy",

