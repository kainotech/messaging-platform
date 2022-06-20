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
            "Authorization":"Bearer EAAGpo6XqllQBAJiD1woxLQMpPDLiCMM4SMBMMf8lZCFnhkP71TmwYZC34dcNeIVpussE95V0ZAPJephMCYS2lCC5UnAPtSvbqNmYftKqpWaOg6L43i0rZCiZABTDT1GVKzCmY8ibVYZB6KBOEdOac8yzfNTZBB07NbaJr5w0AoBek7KhIJopQsN",
        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params()        


    def _make_body_params(self) -> dict:
        _body = {
                "messaging_product": "whatsapp",
                "to": "94701613315",
                "type": "text",
                "text": {
                    "body": "test message by kainovation",
                }
            }
        return _body



    def send(self) -> dict:
        response = self.session.post(
                self.BASE_URL, json=self.req_body, verify=True, allow_redirects=False
            )

        if response.status_code==200:
            return response.text
        


    def message(self):
        res = self.send() 
        return res
