# 4f5acb4ff627e040-a7062fd70d670f24-df614826fe3944f
# 4f5acc5880a7e28c-ce251fcabe617eb9-7bb2fbdbccf272de


from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
	name='Saranga Bakery',
	avatar='http://viber.com/avatar.jpg',
	auth_token='4f5acb4ff627e040-a7062fd70d670f24-df614826fe3944f'
)
viber = Api(bot_configuration)


from viberbot.api.messages import (
    TextMessage,
    ContactMessage,
    PictureMessage,
    VideoMessage
)
from viberbot.api.messages.data_types.contact import Contact

# creation of text message
text_message = TextMessage(text="sample text message!")


# creation of contact message
contact = Contact(name="Saranga", phone_number="94701613315")
contact_message = ContactMessage(contact=contact)


# creation of picture message
picture_message = PictureMessage(text="Check this", media="http://site.com/img.jpg")

# creation of video message
video_message = VideoMessage(media="http://mediaserver.com/video.mp4", size=4324)
