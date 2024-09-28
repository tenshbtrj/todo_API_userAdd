from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api', methods=['POST'])
def post_data():
    data = request.json
    return jsonify({'received': data}), 201

if __name__ == '__main__':
    app.run(debug=True)
