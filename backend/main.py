from lib2to3.pgen2 import token
import re
from fastapi import FastAPI
from src.dialog_api import DialogApi
from src.whatsapp_api import WhatsappApi
from src.telegram_api import TelegramApi
from src.viber_api import ViberApi
from src.models import Platform,dialog_message
import uvicorn


app = FastAPI()


@app.get("/")
def root():
    return "Message api running!"

@app.post("/sendMessageDialog/")
async def send_message(message:str):
    api=DialogApi()
    response=api.message(message=message)
    print(response)
    return response

@app.post("/sendWAMessage/")
async def send_wa_message():
    wa_api=WhatsappApi()
    res=wa_api.message()
    return res

@app.post("/sendTelMessage/")
async def send_tel_message():
    tel_api=TelegramApi()
    res=tel_api.message("Test Message")
    return res

@app.post("/sendViberMessage/")
async def viber_message():
    viber_api=ViberApi()
    res=viber_api.message()
    return res



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)