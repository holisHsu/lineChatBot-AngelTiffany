
import os

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from bot.setting import handler, line_bot_api
from bot.soldier_line_report_record.core import handle_soldier_line_report


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.reply_token == '00000000000000000000000000000000':
        # Pass the invalid token that happen in URL Verifying of Webhook
        # Or it will trigger Exception
        return

    handle_soldier_line_report(event)
