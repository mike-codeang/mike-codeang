# -*- coding: utf-8 -*-

def chatbot(question):
    # Κανονικοποίηση σε lowercase για να μη χαλάει με κεφαλαία
    q = question.lower().strip()

    responses = {
        # Ελληνικά
        "πώς σε λένε;": "Με λένε ChatGPT.",
        "τι κάνεις;": "Είμαι εδώ για να σε βοηθήσω!",
        "ποιος είναι ο δημιουργός σου;": "Με δημιούργησε η OpenAI.",
        "ποια είναι η πρωτεύουσα της ελλάδας;": "Η πρωτεύουσα της Ελλάδας είναι η Αθήνα.",
        "ποιος είναι ο μεγαλύτερος ποταμός στον κόσμο;": "Ο μεγαλύτερος ποταμός στον κόσμο είναι ο Νείλος.",

        # Greeklish
        "pos se lene?": "Με λένε ChatGPT.",
        "ti kaneis?": "Είμαι εδώ για να σε βοηθήσω!",
        "poios einai o dimiourgos sou?": "Με δημιούργησε η OpenAI.",
        "poia einai i protevousa tis elladas?": "Η πρωτεύουσα της Ελλάδας είναι η Αθήνα.",
        "poios einai o megalyteros potamos ston kosmo?": "Ο μεγαλύτερος ποταμός στον κόσμο είναι ο Νείλος."
    }

    return responses.get(q, "Συγγνώμη, δεν καταλαβαίνω την ερώτησή σου.")


# -------------------------
# Main loop
# -------------------------
if __name__ == "__main__":
    while True:
        question = input("Ρώτησέ με κάτι (ή γράψε 'exit' για έξοδο): ")
        if question.lower() in ["exit", "quit"]:
            print("Αντίο! 👋")
            break
        answer = chatbot(question)
        print("Chatbot:", answer)
