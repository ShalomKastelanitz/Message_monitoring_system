from flask import Flask, request, jsonify
from collections import Counter
import json

from Message_monitoring_system.Service.service import get_email_with_suspicious_content
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

@app.route('/api/Finding_object', methods=['POST'])
def Finding_object():
    data = request.data.decode('utf-8')
    return jsonify(  get_email_with_suspicious_content(data)), 200


@app.route('/api/Finding_suspicious_content', methods=['POST'])
def Finding_most_common_word():
    data = request.data.decode('utf-8')
    print(data)
    return jsonify(    get_email_with_suspicious_content(data)), 200

if __name__ == '__main__':
    app.run(debug=True)


