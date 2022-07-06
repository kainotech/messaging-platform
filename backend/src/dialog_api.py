from email import message
import os
import json
from fastapi import File
import requests
import os
import shutil
import pandas as pd


#single message
class DialogApi():
    class_name = os.path.basename(__file__)

    def __init__(self) -> None:
        self.BASE_URL = "https://e-sms.dialog.lk/api/v1/login"

        self.session = requests.Session()
        self.req_headers = {
            "content-type": "application/json"
        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params()        


    def _make_body_params(self) -> dict:
        _body = {
                "username": "saranga99",
                "password": "Saranga@1234"
        }
        return _body
    
    def get_transaction_id(self) -> int:
        with open ("src/transaction_id.txt", "r") as myfile:
            prev_id = myfile.read()
            new_id=int(prev_id)+1
        
        file = open("src/transaction_id.txt","w")
        file.write(str(new_id))
        file.close() 

        return new_id

    def _make_body_params_message(self,message) -> dict:
        _body = {
                    "sourceAddress": "kainovation",
                    "message": message,
                    "transaction_id": self.get_transaction_id(),
                    "msisdn": [{"mobile": "0701613315"}]
                }
        return _body

    def get_token(self) -> dict:
        response = self.session.post(
                self.BASE_URL, json=self.req_body, verify=True, allow_redirects=False
            )

        if response.status_code==200:
            return json.loads(response.text)["token"]
        
    def sending_message(self,token,message):
        self.BASE_URL = "https://e-sms.dialog.lk/api/v1/sms"

        self.session = requests.Session()
        self.req_headers = {
            "Authorization":"Bearer "+token,
            "content-type": "application/json"
        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params_message(message)
        response = self.session.post(
                self.BASE_URL, json=self.req_body, verify=True, allow_redirects=False
            )

        if response.status_code==200:
            return response.text


    def message(self,message:str):
        token = self.get_token()
        res=self.sending_message(token,message)
        return res




#bulk messages from csv
class DialogApiBulk():
    class_name = os.path.basename(__file__)

    def __init__(self) -> None:
        self.BASE_URL = "https://e-sms.dialog.lk/api/v1/login"

        self.session = requests.Session()
        self.req_headers = {
            "content-type": "application/json"
        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params()        


    def _make_body_params(self) -> dict:
        _body = {
                "username": "saranga99",
                "password": "Saranga@1234"
        }
        return _body
    
    def get_transaction_id(self) -> int:
        with open ("src/transaction_id.txt", "r") as myfile:
            prev_id = myfile.read()
            new_id=int(prev_id)+1
        
        file = open("src/transaction_id.txt","w")
        file.write(str(new_id))
        file.close() 

        return new_id

    #temp locations
    def dir(self):
        temp="temp/"
        os.makedirs(temp,exist_ok=True)


    def get_number_list(self,file):
        self.dir()
        #need to change all things to src
        file_location = f"temp/{file.filename}"

        with open(file_location, "wb+") as file_object:
            shutil.copyfileobj(file.file, file_object)  

        df = pd.read_csv(file_location)
        df["numbers"]  = df["numbers"].astype(str)
        print(df)
        numbers = df["numbers"].tolist()

        msisdn=[]
        for number in numbers:
            msisdn.append({"mobile" : number})

        shutil.rmtree("temp")
        return msisdn


    def _make_body_params_message(self,message,number_list) -> dict:
        _body = {
                    "sourceAddress": "kainovation",
                    "message": message,
                    "transaction_id": self.get_transaction_id(),
                    "msisdn": number_list
                }
        return _body

    def get_token(self) -> dict:
        response = self.session.post(
                self.BASE_URL, json=self.req_body, verify=True, allow_redirects=False
            )

        if response.status_code==200:
            return json.loads(response.text)["token"]
        
    def sending_message(self,token,message,file):
        self.BASE_URL = "https://e-sms.dialog.lk/api/v1/sms"

        self.session = requests.Session()
        self.req_headers = {
            "Authorization":"Bearer "+token,
            "content-type": "application/json"
        }
        self.session.headers.update(self.req_headers)
        numbers = self.get_number_list(file)
        self.req_body = self._make_body_params_message(message,numbers)
        response = self.session.post(
                self.BASE_URL, json=self.req_body, verify=True, allow_redirects=False
            )

        if response.status_code==200:
            return response.text


    def message(self,message:str,file):
        token = self.get_token()
        res=self.sending_message(token,message,file)
        return res
