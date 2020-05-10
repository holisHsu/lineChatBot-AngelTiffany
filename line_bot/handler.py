
import os

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


CHANNEL_ACCESS_TOKEN = os.environ.get('CHANNEL_ACCESS_TOKEN', '')
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET', '')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.reply_token == '00000000000000000000000000000000':
        # Pass the invalid token that happen in URL Verifying of Webhook
        # Or it will trigger Exception
        return

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
