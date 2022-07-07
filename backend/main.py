from lib2to3.pgen2 import token
import re
from fastapi import FastAPI, File, UploadFile
from src.dialog_api import DialogApi, DialogApiBulk
from src.whatsapp_api import WhatsappApi, WhatsappApiBulk
from src.telegram_api import TelegramApi
from src.viber_api import ViberApi
from src.models import Platform,dialog_message
from tempfile import NamedTemporaryFile
import uvicorn
import csv
import os


app = FastAPI()

#root
@app.get("/")
def root():
    return "Message api running!"

#dialog message
@app.post("/sendMessageDialog/")
async def send_message(number:str,message:str):
    api=DialogApi()
    response=api.message(message=message,number=number)
    print(response)
    return response

#dialog bulk messages
@app.post("/sendBulkDialog")
async def send_bulk_dialog(file: UploadFile = File(...),message:str="test message"):
    api = DialogApiBulk()
    response = api.message(message=message,file=file)
    return response

#whatsapp message
@app.post("/sendWA/")
async def send_wa_message(business_id:str="105726822204079",number:str=""):
    wa_api=WhatsappApi(business_id,number)
    res=wa_api.message()
    return res

#whatsapp bulk messages
@app.post("/sendWAMBulk")
async def send_bulk_dialog(file: UploadFile = File(...),business_id:str="105726822204079"):
    api = WhatsappApiBulk(business_id,file)
    response = api.message()
    return response

#telegram bot
@app.post("/sendTelMessage/")
async def send_tel_message():
    tel_api=TelegramApi()
    res=tel_api.message("Test Message")
    return res

#viber bot
@app.post("/sendViberMessage/")
async def viber_message():
    viber_api=ViberApi()
    res=viber_api.message()
    print(res)
    return res
















if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)