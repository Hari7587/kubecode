from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi Harish H Wellcome to the web world'
