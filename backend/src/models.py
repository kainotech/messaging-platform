from pydantic import BaseModel, Field, ValidationError, validator
from enum import Enum



class Platform(str, Enum):
    dialog = "dialog"
    mobitel = "mobitel"
    whatsapp = "whatsapp"