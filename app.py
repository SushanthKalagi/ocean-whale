from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/system/check', methods=['GET'])
def system_check():
    return jsonify({"message": "Service is up and running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)