from kafka import KafkaConsumer
import json

from datetime import datetime

from Message_monitoring_system.db.PostgreSQL import Email, session, SuspiciousHostageContent, SuspiciousExplosiveContent

# הגדרת צרכן Kafka לנושאים "messages.hostage" ו-"messages.explosive"
consumer_suspicious = KafkaConsumer(
    'messages.hostage', 'messages.explosive',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Starting suspicious content consumer for PostgreSQL...")

for message in consumer_suspicious:
    email_data = message.value
    topic = message.topic
    print(email_data)

    # יצירת אובייקט אימייל
    email_entry = Email(
        id=email_data['id'],
        email_address=email_data.get("email"),
        username=email_data.get("username"),
        ip_address=email_data.get("ip_address"),
        created_at=datetime.fromisoformat(email_data.get("created_at")),
        location=email_data.get("location"),
        device_info=email_data.get("device_info")
    )
    session.add(email_entry)
    session.commit()  # שמירת ה-email_entry כך שנוכל לקשר אליו משפטים חשודים

    # הכנסת משפטים חשודים לטבלאות בהתאם לנושא ההודעה
    suspicious_sentences = email_data.get("sentences", [])
    if topic == "messages.hostage":
        for sentence in suspicious_sentences:
            entry = SuspiciousHostageContent(email_id=email_entry.id, suspicious_sentence=sentence)
            session.add(entry)
    elif topic == "messages.explosive":
        for sentence in suspicious_sentences:
            entry = SuspiciousExplosiveContent(email_id=email_entry.id, suspicious_sentence=sentence)
            session.add(entry)

    session.commit()
    print(f"Suspicious content from '{topic}' saved to PostgreSQL.")
    print(str(entry))


