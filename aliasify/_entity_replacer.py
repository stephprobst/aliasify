"""EntityReplacer class to replace entities with placeholders."""
from sys import stderr
import spacy

class EntityReplacer:
    """Replace entities with placeholders."""
    entities_to_replace = [
        "DATE",
        "EVENT",
        "FAC",
        "GPE",
        "LANGUAGE",
        "LAW",
        "LOC",
        "MONEY",
        "NORP",
        "ORG",
        "PERCENT",
        "PERSON",
        "PRODUCT",
        "QUANTITY",
        "TIME",
        "WORK_OF_AR",
    ]

    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_trf")
        except OSError:
            print('Downloading spacy language model to detect entities.\n'
                "(This will only happen during the first usage.)", file=stderr)
            from spacy.cli import download #pylint: disable=import-outside-toplevel
            download("en_core_web_trf")
            self.nlp = spacy.load('en_core_web_trf')

        self.entity_dict = {}
        self.counter = 1

    def replace_entities(self, text):
        """Replace entities with placeholders."""
        doc = self.nlp(text)
        placeholder_text = text
        for entity in doc.ents:
            if entity.label_ not in EntityReplacer.entities_to_replace:
                continue
            placeholder = "<<" + entity.label_ + "_" + f"{self.counter:0>6}" + ">>"
            placeholder_text = placeholder_text.replace(entity.text, placeholder)
            self.entity_dict[placeholder] = entity.text
            self.counter += 1
        return placeholder_text

    def restore_entities(self, text):
        """Restore placeholders with original values."""
        restored_text = text
        for placeholder, entity in self.entity_dict.items():
            restored_text = restored_text.replace(placeholder, entity)
        return restored_text