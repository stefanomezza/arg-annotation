from flask import Flask
import os
from flask_cors import CORS
from flask import request
import json
from flask import send_from_directory

app = Flask(__name__)
CORS(app)
players = {}


EXPERIMENTS = {
    "89h13r89pj": "bulbasaur.json",
    "90uqj3riop": "charmander.json",
    "w8huriopaf": "pikachu.json",
    "89ph43q8tq": "squirtle.json",
    'pilot': "pilot.json"
}


@app.route('/send_response', methods=['POST'])
def send_response():
    content = request.data
    content = json.loads(content)
    password = content['pass']
    with open(f"data/{EXPERIMENTS[password]}") as f:
        exp = json.load(f)
    k = list(content['response'].keys())[0]
    exp_name, exp_idx = k.split("__")
    v = list(content['response'].values())[0]
    exp[exp_name][exp_idx] = v
    with open(f"data/{EXPERIMENTS[password]}", 'w') as f:
        json.dump(exp, f, indent=4)
    return json.dumps({'res': 'ok'})


@app.route('/get_data', methods=['POST'])
def get_data():
    content = request.data
    content = json.loads(content)
    password = content['pass']
    if password not in EXPERIMENTS.keys():
        return json.dumps({"res": "no_exp", 'data': {}})
    print("get data")
    with open(f'data/{EXPERIMENTS[password]}') as f:
        content = json.load(f)
    print("returning content")
    return json.dumps({'res': 'ok', 'data': content})


@app.route('/<path:path>')
def serve_static(path):
        return send_from_directory('static/', path)


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0', port=1234)
    except KeyboardInterrupt:
        print('Server stopped manually')
