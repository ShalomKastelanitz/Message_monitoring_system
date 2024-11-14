from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def Producer_Sending_all(data):
    producer.send('messages.all', data)
    print("Producer_Sending_all")


suspicious_keywords = {
    "hostage": "messages.hostage",
    "explos": "messages.explosive"
}

def send_to_suspicious_topic(data):
    text_content = " ".join(data.get("sentences", []))
    for keyword, topic in suspicious_keywords.items():
        if keyword in text_content :
            producer.send(topic, data)
            print(f"Suspicious content found: {keyword}. Sent to topic: {topic}")

