
import logging

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


logger = logging.getLogger(__name__)
app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = 'GPG2p6cOelYZLsnEf4zE6TthrttjtwRgTbF1wKZ9bgQhdyIUVUOJnPNpqiAtS/pqWR7/GBYeGmIKaPZNBkVX2Cj3QMgAqlrYZdwhaVYWh63S1IrZmgdQnpOI+El/xG+ucqkHaqrLuPb5p08ZqoH5WgdB04t89/1O/w1cDnyilFU='
CHANNEL_SECRET = '551414750789da2305b7381d404a40d8'

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/", methods=['GET'])
def detect_alive():
    return "ArmyAngel Server is runing"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if hasattr(event, 'reply_token') is False:
        return  # Do nothing if we can not reply

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
