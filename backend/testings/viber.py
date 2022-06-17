from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage
from viberbot import Api

bot_configuration = BotConfiguration(
	name='Saranga Bakery',
	avatar='https://media-direct.cdn.viber.com/pg_download?pgtp=icons&dlid=0-04-01-50bcec73dcd00b7612fbe9d12f5ba644421e1493f2f02bde7323f71ef9c70607&fltp=jpg&imsz=0000',
	auth_token='4f5acb4ff627e040-a7062fd70d670f24-df614826fe3944f'
)
viber = Api(bot_configuration)
print(viber)

account_info = viber.get_account_info()
print(account_info)

print(viber)

event_types = viber.set_webhook('https://webhook.site/adfd9aa5-202a-47cd-8fab-9d28ae2f4a94')

# tokens = viber.send_messages(to="v0VTGJ1gxendIFHjWx4oZQ==",messages=[TextMessage(text="sample message")])

