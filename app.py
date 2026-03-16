# app.py
import os

from flask import Flask, send_file
import threading
import qrcode
import requests
from dotenv import load_dotenv
import time
load_dotenv()

DEVICE_CODE = os.getenv("DEVICE_CODE")
API_URL = os.getenv("API_URL")

app = Flask(__name__)

@app.route("/image")
def image():
    return send_file("images/current.png", mimetype="image/png")

@app.route("/")
def index():
    return """
    <html>
        <body>
            <img id="img" src="/image" width="400">
            <script>
                setInterval(function(){
                    document.getElementById("img").src = "/image?t=" + new Date().getTime();
                }, 2000);
            </script>
        </body>
    </html>
    """

def generate_loop():
    while True:
        try:
            response = requests.get(API_URL + "/check_in_code", headers={"device-code": DEVICE_CODE})
            data = response.json()
            code = data[0]["code"]
            img = qrcode.make(code)
            img.save("images/current.png")
        except Exception as e:
            print(f"Error generating QR code: {e}")
        time.sleep(2)

threading.Thread(target=generate_loop, daemon=True).start()

app.run(host="0.0.0.0", port=5000)