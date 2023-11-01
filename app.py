from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi Wellcome you all a Happy 68th Karnataka Rajyotsava 2023'
