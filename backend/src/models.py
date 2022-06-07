from pydantic import BaseModel, Field, ValidationError, validator
from enum import Enum



class Platform(str, Enum):
    dialog = "dialog"
    mobitel = "mobitel"
    whatsapp = "whatsapp"


class dialog_message(BaseModel):
    message: str="Test SMS(Dialog) by Kainovation"

