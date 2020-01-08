from flask import Flask
import os
#import socket

app = Flask(__name__)
IPAddr = os.environ.get("MY_POD_IP")

@app.route("/")
def hello():
     return "Hello Paygate! This is from Pod -" + IPAddr 


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
