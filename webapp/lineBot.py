# Channel secret : 8adfd81678a48c45933988bbedaf5b9d
# Bot basic ID : @084qcmhm
# Channel access token : YRcrCa3LD+iJa4BLJqPXkKtbPFSVrGQNIVZTRU0YAecznUMB8hKYiY2T4Mw61A58dAVwGaKI2ZqwJQ0HMfWdXgT0ka2VYYx/KBOKWrRnxcVdOJaNQbuI3YYCpTdDqFyswGV7Xf5OLDrrAoY2lnRhaAdB04t89/1O/w1cDnyilFU=
# pip install line-bot-sdk
from pyngrok import ngrok, conf

# 設定token
# ngrok.set_auth_token("申請的AuthToken")
ngrok.set_auth_token("2I7AQZ52Bb38Qlupu8410rWxOB6_35cjKC5gk5q2qnAhfv1er")
conf.get_default().region = "jp"

def connNgrok():
    port = 5000
    public_url = ngrok.connect(port, bind_tls=True).public_url
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(public_url, port))

# 測試連線
# from flask import Flask
# connNgrok()
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Hello World"

# if __name__ == '__main__':
#     app.run()

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

connNgrok()
app = Flask(__name__)

line_bot_api = LineBotApi('YRcrCa3LD+iJa4BLJqPXkKtbPFSVrGQNIVZTRU0YAecznUMB8hKYiY2T4Mw61A58dAVwGaKI2ZqwJQ0HMfWdXgT0ka2VYYx/KBOKWrRnxcVdOJaNQbuI3YYCpTdDqFyswGV7Xf5OLDrrAoY2lnRhaAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8adfd81678a48c45933988bbedaf5b9d')


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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()