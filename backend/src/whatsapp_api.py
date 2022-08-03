import os
import json
import requests
import shutil
import pandas as pd
import asyncio
import aiohttp
import nest_asyncio
nest_asyncio.apply()

# 94741878798
# 0705815179
# permant token
# EAAGpo6XqllQBADq2XbZBCxunt3lEw6RW7fy7V7ZB6inUXTGgZANHNKCtGTTmIYpZBgW6vmSaMCpCoaF3mac8eFvtm0vcivW3umSlyBls7vREjiBIG7BXft2hZCL2uhZAJlYA4b4RAYZCps2Pw3zz9DGwMYeN9GbsutvqLTN05iNAwteQKrIzD3dZAbfK3iT8ZCC7XC9OzxSBmZBwZDZD
token = "EAAGpo6XqllQBADq2XbZBCxunt3lEw6RW7fy7V7ZB6inUXTGgZANHNKCtGTTmIYpZBgW6vmSaMCpCoaF3mac8eFvtm0vcivW3umSlyBls7vREjiBIG7BXft2hZCL2uhZAJlYA4b4RAYZCps2Pw3zz9DGwMYeN9GbsutvqLTN05iNAwteQKrIzD3dZAbfK3iT8ZCC7XC9OzxSBmZBwZDZD"
class WhatsappApi():
    class_name = os.path.basename(__file__)

    def __init__(self,business_id:str,number:str) -> None:
        # self.BASE_URL = "https://graph.facebook.com/v13.0/105726822204079/messages"
        self.BASE_URL = f"https://graph.facebook.com/v13.0/{business_id}/messages"
        self.session = requests.Session()
        self.req_headers = {
            "content-type": "application/json",
            "Authorization":"Bearer "+token,
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




class WhatsappApiBulk():
    class_name = os.path.basename(__file__)
    def __init__(self,business_id:str,file) -> None:
        dir()
        self.number_list = self.get_number_list(file)
        self.BASE_URL = f"https://graph.facebook.com/v13.0/{business_id}/messages"
        self.results = []

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

        shutil.rmtree("temp")
        return numbers


    def get_tasks(self,session,number_list):
        tasks = []
        for number in number_list:
            tasks.append(asyncio.create_task(session.post(
            url=self.BASE_URL, 
            headers={
                "content-type": "application/json",
                "Authorization":"Bearer "+token,
            },
            json={
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
                },
            ssl=False)))
        return tasks


    async def get_symbols(self,number_list):
        async with aiohttp.ClientSession() as session:
            tasks = self.get_tasks(session,number_list)
            responses = await asyncio.gather(*tasks)
            for response in responses:
                self.results.append(await response.text())


    def message(self):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.get_symbols(self.number_list))
        print(f"{len(self.number_list)} api calls sent")  
        # loop.close()