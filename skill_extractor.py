import spacy
nlp = spacy.load("en_core_web_sm")

def extract_skills(text, skill_db):
    doc = nlp(text)
    found = set()

    for token in doc:
        if token.text.lower() in skill_db:
            found.add(token.text.lower())

    return list(found)
