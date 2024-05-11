from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import time

# import sensor


# app = Flask(__name__,template_folder='../frontend/dist')
app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/sensor')
def hello():
    # name = "Hello World"
    # val = sensor.get_val()
    val = 1
    return {'val': val}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

## おまじない
if __name__ == "__main__":
    app.run(debug=True, port=5053, host='0.0.0.0')