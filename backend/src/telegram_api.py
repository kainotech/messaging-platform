import os
import telepot


class TelegramApi():
    class_name = os.path.basename(__file__)

    def __init__(self) -> None:
      self.api_id = "16614431"
      self.api_hash = '48f640ce7e1dc5b434d2f382dddac989'
      self.bot_token = '5471537894:AAGQe_UHJNHqP_6UsZcGp5Ndt0DAgwbAQAE'
 

    def message(self,message:str):
        bot=telepot.Bot(self.bot_token)
        bot.sendMessage(1090822693,"Hi there\nthis is test message")    
