from kafka import KafkaConsumer
import json

from Message_monitoring_system.db.mongo import mongo_collection

consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)




for message in consumer:
    email_data = message.value
    mongo_collection.insert_one(email_data)
    print(f"Email data saved to MongoDB: {email_data}")
