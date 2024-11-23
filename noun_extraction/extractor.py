import re
import spacy

nlp = spacy.load("uk_core_news_sm")

def extract_nouns(text):
    doc = nlp(text)
    nouns = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']]  # Include both common and proper nouns
    return nouns


