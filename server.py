from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8914918786:AAFaQZek5qpLLxf2foCXkULVfn2Anaq_lAg"
CHAT_ID = "8738009031"

@app.route('/')
def index():
    return "Bot is active"

@app.route('/data', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        msg = request.data.decode()
    else:
        msg = request.args.get('msg', 'GET request test')
    
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg})
        return "OK"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
