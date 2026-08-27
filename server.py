from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8914918786:AAFaQZek5qpLLxf2foCXkULVfn2Anaq_lAg"
CHAT_ID = "8738009031"

@app.route('/')
def index():
    return "Bot is active"

@app.route('/data', methods=['POST'])
def send_message():
    msg = request.data.decode()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, json=data)
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
