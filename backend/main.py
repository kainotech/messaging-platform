from lib2to3.pgen2 import token
import re
from fastapi import FastAPI
from src.dialog_api import DialogApi
from src.whatsapp_api import WhatsappApi

app = FastAPI()


@app.get("/")
def root():
    return "Message api running!"

@app.post("/sendMessage/")
async def send_message():
    api=DialogApi()
    response=api.message()
    print(response)

@app.post("/sendWAMessage/")
async def send_wa_message():
    wa_api=WhatsappApi()
    res=wa_api.message()
    print(res)
