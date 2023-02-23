import spacy
from pynput import keyboard
import pyperclip as pc
from win10toast import ToastNotifier

toaster = ToastNotifier()

nlp = spacy.load("en_core_web_trf")

entitites_to_replace = [
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

entity_dict = {}
counter = 1


def on_replace():
    print("Replace triggered...")
    toaster.show_toast(
        "Replace triggered",
        "The entities in your clipboard have been replaced with placeholders. The original values have been saved.",
        duration=3,
        threaded=True,
    )
    global entity_dict
    global counter
    text = pc.paste()
    doc = nlp(text)
    placeholder_text = text

    for entity in doc.ents:
        if entity.label_ not in entitites_to_replace:
            continue
        placeholder = "<<" + entity.label_ + "_" + "{:0>{}}".format(counter, 6) + ">>"
        placeholder_text = placeholder_text.replace(entity.text, placeholder)
        entity_dict[placeholder] = entity.text
        counter += 1
    pc.copy(placeholder_text)


def on_restore():
    print("Restore triggered...")
    toaster.show_toast(
        "Restore triggered",
        "The placeholders in your clipboard have been replaced with the original values.",
        duration=3,
        threaded=True,
    )
    global entity_dict
    text = pc.paste()
    if text is None:
        return
    restored_text = text
    for placeholder, entity in entity_dict.items():
        restored_text = restored_text.replace(placeholder, entity)
    pc.copy(restored_text)


def on_press(key):
    if key == keyboard.Key.f9:
        on_replace()
    elif key == keyboard.Key.f10:
        on_restore()


with keyboard.Listener(on_press=on_press) as listener:
    print("Ready..")
    listener.join()
