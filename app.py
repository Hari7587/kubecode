from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi Harish&Suma Wellcomes you all a Happy 68th Kannada Rajyotsava..!'
