import tkinter as tk
import threading
import winsound
import os
import sys

from pynput import mouse, keyboard


# ============================================================
# AUDIO RESOURCE CONFIGURATION
# ============================================================

def resource_path(filename):

    # When the application is built with PyInstaller.
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS

    # When running the Python script directly.
    else:
        base_path = os.path.dirname(
            os.path.abspath(__file__)
        )

    return os.path.join(
        base_path,
        filename
    )


SOUND_FILE = resource_path("salahor.wav")


# ============================================================
# VARIABILE
# ============================================================

running = True


# ============================================================
# PLAY SOUND
# ============================================================

def play_sound():

    if not running:
        return

    try:

        winsound.PlaySound(
            SOUND_FILE,
            winsound.SND_FILENAME |
            winsound.SND_ASYNC
        )

    except Exception as error:

        print(f"Sound error: {error}")


# ============================================================
# GLOBAL CLICK
# ============================================================

def on_click(
    x,
    y,
    button,
    pressed
):

    if not running:
        return False

    # Play the sound when a mouse button is pressed.
    if pressed:

        play_sound()


# ============================================================
# STOP PROGRAM
# CTRL + SHIFT + L + A
# ============================================================

def stop_program():

    global running

    if not running:
        return

    running = False

    print("Program stopped.")

    root.after(
        0,
        root.destroy
    )


# ============================================================
# START MOUSE LISTENER
# ============================================================

def start_mouse_listener():

    with mouse.Listener(
        on_click=on_click
    ) as listener:

        listener.join()


# ============================================================
# START GLOBAL HOTKEY LISTENER
# ============================================================

def start_keyboard_listener():

    with keyboard.GlobalHotKeys({

        "<ctrl>+<shift>+l+a":
            stop_program

    }) as listener:

        listener.join()


# ============================================================
# START PROGRAM
# ============================================================

root = tk.Tk()

# Do not show a window in the taskbar.
root.withdraw()


# ============================================================
# MOUSE LISTENER
# ============================================================

mouse_thread = threading.Thread(
    target=start_mouse_listener,
    daemon=True
)

mouse_thread.start()


# ============================================================
# KEYBOARD LISTENER
# ============================================================

keyboard_thread = threading.Thread(
    target=start_keyboard_listener,
    daemon=True
)

keyboard_thread.start()


# ============================================================
# MENȚINE PROGRAMUL ACTIV
# ============================================================

print("MouseClick is running.")
print(f"Audio file: {SOUND_FILE}")
print("Press Ctrl+Shift+L+A to stop the program.")

root.mainloop()