from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import album

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Lenny!"}), 200

@app.route('/albums', methods=['GET', 'POST'])
def albums_handler():
    fns = {
        'GET': album.index,
        'POST': album.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)