import telepot
api_id = "16614431"
api_hash = '48f640ce7e1dc5b434d2f382dddac989'
bot_token = '5471537894:AAGQe_UHJNHqP_6UsZcGp5Ndt0DAgwbAQAE'
# We have to manually call "start" if we want an explicit bot token
# bot = TelegramClient('testing_kaino_bot', api_id, api_hash).start(bot_token=bot_token)
# But then we can use the client instance as usual
# bot.send_message(0000000,"hii")

bot=telepot.Bot(bot_token)
bot.sendMessage(1090822693,"Hi there\nthis is test message")

# https://api.telegram.org/bot5471537894:AAGQe_UHJNHqP_6UsZcGp5Ndt0DAgwbAQAE/getUpdates