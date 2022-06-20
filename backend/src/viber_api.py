import os
import json
import requests
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot import Api
import requests
import json


class ViberApi():
    class_name = os.path.basename(__file__)

    def __init__(self) -> None:
        self.BASE_URL = "https://chatapi.viber.com/pa/send_message"

        self.session = requests.Session()
        self.req_headers ={'Content-Type': 'application/json',
                            "X-Viber-Auth-Token":"4f5acb4ff627e040-a7062fd70d670f24-df614826fe3944f"
                        }
        self.session.headers.update(self.req_headers)
        self.req_body = self._make_body_params()        


    def _make_body_params(self) -> dict:
        _body = {
                "receiver":"v0VTGJ1gxendIFHjWx4oZQ==",
                "min_api_version":1,
                "sender":{
                    "name":"Saranga Bakery",
                    "avatar":"https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/0607/50bcec73dcd00b7612fbe9d12f5ba644421e1493f2f02bde7323f71ef9c70607.jpg"
                },
                "tracking_data":"tracking data",
                "type":"text",
                "text":"Testing Message By Kainovation"
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


###




# url='https://chatapi.viber.com/pa/set_webhook'

# data ={
# 			"url":"https://webhook.site/adfd9aa5-202a-47cd-8fab-9d28ae2f4a94",
# 			"event_types":[
# 				"delivered",
# 				"seen",
# 				"failed",
# 				"subscribed",
# 				"unsubscribed",
# 				"conversation_started"
# 			],
# 			"send_name": True,
# 			"send_photo": True
# 			}

# r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json',"X-Viber-Auth-Token":"4f5acb4ff627e040-a7062fd70d670f24-df614826fe3944f"})
# print("\nresponse\n"+r.text)
# # tokens = viber.send_messages(to="v0VTGJ1gxendIFHjWx4oZQ==",messages=[TextMessage(text="sample message")])



# url='https://chatapi.viber.com/pa/send_message'

# data ={
# 		"receiver":"v0VTGJ1gxendIFHjWx4oZQ==",
# 		"min_api_version":1,
# 		"sender":{
# 			"name":"Saranga Bakery",
# 			"avatar":"https://dl-media.viber.com/1/share/2/long/vibes/icon/image/0x0/0607/50bcec73dcd00b7612fbe9d12f5ba644421e1493f2f02bde7323f71ef9c70607.jpg"
# 		},
# 		"tracking_data":"tracking data",
# 		"type":"text",
# 		"text":"Testing Message By Kainovation"
# 		}

# r = requests.post(url, data=json.dumps(data), headers={'Content-Type': 'application/json',"X-Viber-Auth-Token":"4f5acb4ff627e040-a7062fd70d670f24-df614826fe3944f"})
# print("\nresponse\n"+r.text)