from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi Harish & Suma Wellcome Happy 68th Karnataka Rajyotsava..!'
