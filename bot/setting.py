
import os

from linebot import (
    LineBotApi, WebhookHandler
)

CHANNEL_ACCESS_TOKEN = os.environ.get('CHANNEL_ACCESS_TOKEN', '')
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET', '')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)
