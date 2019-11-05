from w3lib.html import replace_entities, remove_tags
import re


def clean_text(text):

    # Helper function to clean text data and remove non-printable chars.

    text = text.strip()
    text = re.sub(r'[\n\t\r\s]+', ' ', text)
    text = text.encode('ascii', errors='ignore').decode('ascii')
    text = replace_entities(text)
    text = remove_tags(text)
    return text
