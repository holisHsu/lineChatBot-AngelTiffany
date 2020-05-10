
import os
import logging

from flask import Flask, request, abort

from line_bot.handler import handler


logger = logging.getLogger(__name__)
app = Flask(__name__)


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


if __name__ == "__main__":
    app.run()
