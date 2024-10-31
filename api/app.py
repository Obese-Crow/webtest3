from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

current_name = "_______"

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify(name=current_name)

@app.route('/api/message', methods=['POST'])
def post_message():
    global current_name
    data = request.get_json()
    name = data.get('name')
    if name:
        current_name = name
    return jsonify(name=current_name)

# Entry point for Vercel
if __name__ == "__main__":
    app.run()
