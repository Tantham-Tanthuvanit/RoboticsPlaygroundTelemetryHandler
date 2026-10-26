from flask import Flask, jsonify, request

app = Flask(__name__)
latest_data = {"rpm":0.0, "points": [
    {
      "a": 0.0,
      "d": 1245,
      "c": 45
    },
    {
      "a": 1.5,
      "d": 1250,
      "c": 47
    },
    {
      "a": 3.0,
      "d": 1242,
      "c": 44
    }
]}

@app.route("/")
def initialization_msg():
    return "Hello world"

@app.route("/lidar-scan", methods=['POST'])
def recieve_scan():
    global latest_data
    latest_data = request.get_json()
    return jsonify({"status": "recieved"}), 200

@app.route("/lidar-result", methods=['get'])
def return_scan():
    return jsonify(latest_data), 200