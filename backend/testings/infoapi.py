import requests

"""
 * Send WhatsApp template message directly by calling HTTP endpoint.
 *
 * THIS CODE EXAMPLE IS READY BY DEFAULT. HIT RUN TO SEND THE MESSAGE!
 *
 * Send WhatsApp API reference: https://www.infobip.com/docs/api#channels/whatsapp/send-whatsapp-template-message
 *
 * See Readme file for details.
"""

BASE_URL = "https://yrj1e9.api.infobip.com"
API_KEY = "App c494da16ef5f1b481e3ffd994bfcd8fe-7d3eeaa8-9aa9-4741-8109-d24694ecf1f6"

SENDER = "447860099299"
RECIPIENT = "94701613315"

payload = {
    "messages":
        [
            {
                "from": SENDER,
                "to": RECIPIENT,
                "content": {
                    "templateName": "registration_success",
                    "templateData": {
                      "body": {
                        "placeholders": [
                          "sender",
                          "message",
                          "delivered",
                          "testing"
                        ]
                      },
                      "header": {
                        "type": "IMAGE",
                        "mediaUrl": "https://api.infobip.com/ott/1/media/infobipLogo"
                      },
                      "buttons": [
                        {
                          "type": "QUICK_REPLY",
                          "parameter": "yes-payload"
                        },
                        {
                          "type": "QUICK_REPLY",
                          "parameter": "no-payload"
                        },
                        {
                          "type": "QUICK_REPLY",
                          "parameter": "later-payload"
                        }
                      ]
                  },
                  "language": "en"
               }
           }
        ]
    }

headers = {
    'Authorization': API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.post(BASE_URL + "/whatsapp/1/message/template", json=payload, headers=headers)

print(response.json())
