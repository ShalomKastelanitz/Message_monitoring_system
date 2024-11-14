from Message_monitoring_system.db.PostgreSQL import session, Email

def get_email_with_suspicious_content(email_id):
    # שליפת אימייל יחד עם התוכן החשוד
    email = session.query(Email).filter_by(id=email_id).first()
    if not email:
        return None

    email_data = {
        "email_address": email.email_address,
        "username": email.username,
        "ip_address": email.ip_address,
        "created_at": email.created_at,
        "location": email.location,
        "device_info": email.device_info,
        "hostage_sentences": [h.suspicious_sentence for h in email.hostage_content],
        "explosive_sentences": [e.suspicious_sentence for e in email.explosive_content]
    }

    return email_data

def get_email_with_suspicious_content(email_id):
    # שליפת אימייל יחד עם התוכן החשוד
    email = session.query(Email).filter_by(id=email_id).first()
    if not email:
        return None

    email_data = {
        "hostage_sentences": [h.suspicious_sentence for h in email.hostage_content],
        "explosive_sentences": [e.suspicious_sentence for e in email.explosive_content]
    }
print(get_email_with_suspicious_content("7abe2cf7-ed76-43b9-a1ad-4b0643810db3"))
