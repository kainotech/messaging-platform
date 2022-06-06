import os
import json
import requests

# 94741878798

class WhatsappApi():
    class_name = os.path.basename(__file__)

    def __init__(self) -> None:
        self.BASE_URL = "https://graph.facebook.com/v13.0/102050555869182/messages"

        self.session = requests.Session()
        self.req_headers = {
            "content-type": "application/json",
            "Authorization":"Bearer EAAGpo6XqllQBAD71N1x96Mhg5IpcfdeoeZCGh6tQtvONyNRyFZAcdHzrWCsVeneR8LDXFfJhST5ayQzkwaukgKefeBZCgRjfzv2S2WOHYc1kZAMwlZBHtDo6pnGUwPoDJuz9ZBdLpMVpWqE3lHZC1llLVm8O59T1hkxM6c2YQD9jo3r2jSW4Pz3qE5QrXWzDoPZCW6cqW2FlAAZDZD"
        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params()        


    def _make_body_params(self) -> dict:
        _body = {
                "messaging_product": "whatsapp",
                "to": "94701613315",
                "type": "template",
                "template": {
                    "name": "hello_world",
                    "language": {
                        "code": "en_US"
                    }
                }
            }
        return _body



    def send(self) -> dict:
        response = self.session.post(
                self.BASE_URL, json=self.req_body, verify=True, allow_redirects=False
            )

        if response.status_code==200:
            return json.loads(response.text)
        


    def message(self):
        res = self.send() 
        return res
