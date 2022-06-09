# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import datetime


# get your api_id, api_hash, token
# from telegram as described above
api_id = "16614431"
api_hash = "48f640ce7e1dc5b434d2f382dddac989"
token = '5558778607:AAHmlg5wTq8YJ1y8PDEiAeA_QNxjkEAWZnY'
message = "Working..."

# your phone number
phone = "94701613315"

# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session
client.connect()

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():

	client.send_code_request(phone)
	
	# signing in the client
	client.sign_in(phone, input('Enter the code: '))


try:
	# receiver user_id and access_hash, use
	# my user_id and access_hash for reference
	receiver = InputPeerUser('user_id', 'user_hash')

	# sending message using telegram client
	client.send_message(receiver, message, parse_mode='html')
except Exception as e:
	
	# there may be many error coming in while like peer
	# error, wrong access_hash, flood_error, etc
	print(e)

# disconnecting the telegram session
client.disconnect()