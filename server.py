from flask import Flask
import os
from flask_cors import CORS
from flask import request
import json
from flask import send_from_directory

app = Flask(__name__)
CORS(app)
players = {}


EXPERIMENT = "llama-Chat-1_vs_llama-kialo-1.json"


@app.route('/send_response', methods=['POST'])
def check_pass():
    content = request.data
    content = json.loads(content)
    with open(f"data/{EXPERIMENT}") as f:
        exp = json.load(f)
    k = list(content.keys())[0]
    v = list(content.values())[0]
    print(k)
    print(v)
    exp[k] = v
    with open(f"data/{EXPERIMENT}", 'w') as f:
        json.dump(exp, f, indent=4)
    return json.dumps({'res': 'ok'})


@app.route('/get_data', methods=['GET'])
def get_data():
    with open(f'data/{EXPERIMENT}') as f:
        content = json.load(f)
    return json.dumps(content)


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=1234)
    except KeyboardInterrupt:
        print('Server stopped manually')
