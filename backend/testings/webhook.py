import requests
import json

webhook_url = "https://webhook.site/adfd9aa5-202a-47cd-8fab-9d28ae2f4a94"

data = { 'name': 'DevOps Journey', 
         'Channel URL': 'https://www.youtube.com/channel/UC4Snw5yrSDMXys31I18U3gg' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})