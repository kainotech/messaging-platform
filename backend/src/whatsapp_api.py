import os
import json
import requests

# 94741878798
# 0705815179

class WhatsappApi():
    class_name = os.path.basename(__file__)

    def __init__(self,business_id:str,number:str) -> None:
        # self.BASE_URL = "https://graph.facebook.com/v13.0/105726822204079/messages"
        self.BASE_URL = f"https://graph.facebook.com/v13.0/{business_id}/messages"
        self.session = requests.Session()
        self.req_headers = {
            "content-type": "application/json",
            "Authorization":"Bearer EAAGpo6XqllQBABCigcEGvVUamLqBtpxATnTIL0fS3axFGIHKTgJCh0moGZAZCbP0ZB2LIsPZCxHnhJ7Ydl7yRC3ZBmV3oGjWbnAsbTVTNRI5HqYOislS6v2TP7EzosfeZAyRJ1545dsxblQdCu5lySjsW1RkrZCljMCkZAjgRExuqOlvoeqKYcuvxBGWEYN3ZBh1u8HSOqGmjBQZDZD",
        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params(number)        


    def _make_body_params(self,number) -> dict:
        _body = {
                "messaging_product": "whatsapp",
                "to": number,
                "type": "template",
                "template": {
                "name": "sample_shipping_confirmation",
                "language": {
                    "code": "en_US",
                    "policy": "deterministic"
                },
                "components": [
                    {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": "2"
                        }
                    ]
                    }
                ]
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
