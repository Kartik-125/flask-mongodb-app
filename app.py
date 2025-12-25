from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)

MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGODB_URI)

db = client.flask_db
collection = db.data

@app.route("/")
def index():
    return f"Welcome to the Flask app! The current time is: {datetime.now()}"

@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        data = request.get_json()
        collection.insert_one(data)
        return jsonify({"status": "Data inserted"}), 201

    data = list(collection.find({}, {"_id": 0}))
    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

