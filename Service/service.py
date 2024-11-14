from Message_monitoring_system.db.PostgreSQL import session, Email

def get_email_with_suspicious_content(email_1):
    # שליפת אימייל יחד עם התוכן החשוד
    email = session.query(Email).filter_by(email_address=email_1).first()
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

def Finding_most_common_word(email):
    email = session.query(Email).filter_by(email_address=email).first()
    if not email:
        return None

    email_data = {
        "hostage_sentences": [h.suspicious_sentence for h in email.hostage_content],
        "explosive_sentences": [e.suspicious_sentence for e in email.explosive_content]
    }
    data=email_data["hostage_sentences"]+email_data["explosive_sentences"]
    return  Finding_max(data)

print(get_email_with_suspicious_content("7abe2cf7-ed76-43b9-a1ad-4b0643810db3"))
#מוצא את המילה שיש הכי הרבה פעמיים
def Finding_max(text):
    text1 = []
    for txt in text:
        words = txt.split()
        text1.extend(words)

    word_counts = {}
    for word in text1:
        if word[-1] in ",.?;!":
            word = word[:-1]

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    most_common_word = max(word_counts, key=word_counts.get)
    return most_common_word, word_counts[most_common_word]


print(Finding_most_common_word("robert18@example.org"))

