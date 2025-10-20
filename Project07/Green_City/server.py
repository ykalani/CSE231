from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# MongoDB Connection
app.config["MONGO_URI"] = os.getenv("MONGODB_URI", "mongodb://localhost:27017/greenspace")
mongo = PyMongo(app)

# Route to Get All Markers
@app.route('/markers', methods=['GET'])
def get_markers():
    markers = list(mongo.db.markers.find({}, {"_id": 0}))
    return jsonify(markers)

# Route to Add a Marker
@app.route('/add_marker', methods=['POST'])
def add_marker():
    data = request.json
    mongo.db.markers.insert_one(data)
    return jsonify({"message": "Marker added!"}), 201

# Route to Upvote a Marker
@app.route('/upvote', methods=['POST'])
def upvote_marker():
    data = request.json
    marker_id = data['id']
    mongo.db.markers.update_one({"id": marker_id}, {"$inc": {"votes": 1}})
    return jsonify({"message": "Upvoted!"})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
