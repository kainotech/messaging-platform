from telethon.sync import TelegramClient
api_id = "16614431"
api_hash = '48f640ce7e1dc5b434d2f382dddac989'
bot_token = '5471537894:AAGQe_UHJNHqP_6UsZcGp5Ndt0DAgwbAQAE'
# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient('testing_kaino_bot', api_id, api_hash).start(bot_token=bot_token)
# But then we can use the client instance as usual
bot.send_message("94701613315","hii")