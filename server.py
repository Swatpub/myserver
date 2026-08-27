from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8914918786:AAFaQZek5qpLLxf2foCXkULVfn2Anaq_lAg"
CHAT_ID = "8738009031"

@app.route('/data', methods=['POST'])
def receive():
    msg = request.data.decode()
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg})
    except:
        pass
    return "OK"

@app.route('/')
def home():
    return "Server is running!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
