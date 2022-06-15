from lib2to3.pgen2 import token
import re
from fastapi import FastAPI
from src.dialog_api import DialogApi
from src.whatsapp_api import WhatsappApi
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
    print(res)

@app.post("/sendTelMessage/")
async def send_tel_message():
    return "telegram"



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)