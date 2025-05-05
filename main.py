from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

FIREBASE_URL = "https://fanir-c1f7d-default-rtdb.asia-southeast1.firebasedatabase.app/fan.json"

@app.route("/fan", methods=["POST"])
def fan_control():
    data = request.get_json()
    command = data.get("command", "").strip().capitalize()

    if command not in ["Power", "1", "2", "3", "4", "5", "Decrease"]:
        return jsonify({"error": "Invalid command"}), 400

    response = requests.put(FIREBASE_URL, json=command)
    return jsonify({"status": "sent", "firebase_response": response.text})

if __name__ == "__main__":
    app.run()
