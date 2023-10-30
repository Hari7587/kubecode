from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi Harish & Suma Wellcome to the Digital World Of Karnataka..!'
