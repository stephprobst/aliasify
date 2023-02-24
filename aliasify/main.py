"""Main module."""
import pyperclip as pc
from win10toast import ToastNotifier
from pynput import keyboard
from aliasify._entity_replacer import EntityReplacer

_TOASTER = ToastNotifier()

def _on_replace(replacer):
    """Replace entities with placeholders."""
    _show_replace_notification()
    text = pc.paste()
    placeholder_text = replacer.replace_entities(text)
    pc.copy(placeholder_text)


def _on_restore(replacer):
    """Restore placeholders with original values."""
    _show_restore_notification()
    text = pc.paste()
    if text is None:
        return
    restored_text = replacer.restore_entities(text)
    pc.copy(restored_text)


def _show_replace_notification():
    """Show a notification that the replace has been triggered."""
    print("Replace triggered...")
    _TOASTER.show_toast(
        "Replace triggered",
        (
            "The entities in your clipboard are being replaced with placeholders. The"
            " original values have been saved."
        ),
        duration=3,
        threaded=True,
    )

def _show_restore_notification():
    """Show a notification that the restore has been triggered."""
    print("Restore triggered...")
    _TOASTER.show_toast(
        "Restore triggered",
        (
            "The placeholders in your clipboard have been replaced with the original"
            " values."
        ),
        duration=3,
        threaded=True,
    )

def _on_press(key, replacer):
    """Handle key presses."""
    if key == keyboard.Key.f9:
        _on_replace(replacer)
    elif key == keyboard.Key.f10:
        _on_restore(replacer)

def run():
    """Run the main loop."""
    print("Loading language model...")
    replacer = EntityReplacer()
    with keyboard.Listener(on_press=lambda key: _on_press(key, replacer)) as listener:
        print("Ready to replace / restore...")
        listener.join()

if __name__ == "__main__":
    run()
