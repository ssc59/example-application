from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'v4.0.0 - BROKEN VERSION!'

app.run(host='0.0.0.0', port=8080)
