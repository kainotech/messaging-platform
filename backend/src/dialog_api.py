import os
import json
import requests



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

    def _make_body_params_message(self) -> dict:
        _body = {
                    "sourceAddress": "kainovation",
                    "message": "test message from the sms api by kainovation",
                    "transaction_id": self.get_transaction_id(),
                    "msisdn": [
                        {
                            "mobile": "0701613315"
                        }
                    ]
                }
        return _body

    def get_token(self) -> dict:
        response = self.session.post(
                self.BASE_URL, json=self.req_body, verify=True, allow_redirects=False
            )

        if response.status_code==200:
            return json.loads(response.text)["token"]
        
    def sending_message(self,token):
        self.BASE_URL = "https://e-sms.dialog.lk/api/v1/sms"

        self.session = requests.Session()
        self.req_headers = {
            "Authorization":"Bearer "+token,
            "content-type": "application/json"
        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params_message()
        response = self.session.post(
                self.BASE_URL, json=self.req_body, verify=True, allow_redirects=False
            )

        if response.status_code==200:
            return json.loads(response.text)


    def message(self):
        token = self.get_token()
        res=self.sending_message(token)
        return res
