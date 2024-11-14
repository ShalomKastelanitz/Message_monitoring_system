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
            text_content = Finding_most_dangerous_sentence(data["sentences"])
            producer.send(topic, data)
            print(f"Suspicious content found: {keyword}. Sent to topic: {topic}")


def Finding_most_dangerous_sentence(data):
   #בודק איפה יש יותר פעמים
    dangerous_sentence=data[0]
    for  text in data:
        if text.count("explos") > text.count("hostage"):
          if text.count("explos")>dangerous_sentence.count("explos"):
              dangerous_sentence=text


        elif text.count("hostage")>dangerous_sentence.count("hostage"):
             dangerous_sentence=text
     #עושה את ההחלפה
    if len(data) > 0:
        for i in range(len(data)):
            if data[i] == dangerous_sentence:
                data[i] = data[len(data) - 1]
                data[len(data) - 1] = dangerous_sentence
    print(data)
    return data
