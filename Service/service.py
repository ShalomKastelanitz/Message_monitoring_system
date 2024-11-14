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

def Finding_most_common_word(text):
    words = text.split()

    word_counts = {}
    for word in text:
        if word[len(word) - 1] == ',' or word[len(word) - 1] == '.' or word[len(word) - 1] == ';' or word[
            len(word) - 1] == '?' or word[len(word) - 1] == '!':
            word = word[:-1]

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_word = max(word_counts, key=word_counts.get)
    return most_common_word
