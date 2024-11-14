from flask import Flask, request, jsonify
from collections import Counter
import json
from db.mongo import mongo_collection
from Kafka.producer import Producer_Sending_all, send_to_suspicious_topic
app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def receive_email():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    Producer_Sending_all(data)
    send_to_suspicious_topic(data)
    return jsonify(data), 200



if __name__ == '__main__':
    app.run(debug=True)
