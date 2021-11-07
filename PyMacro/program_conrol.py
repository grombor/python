from pynput import keyboard
from mouse_control import set_stop_listening, mouse_start_listening
from points_list import play_list
import sys
from menu import print_menu


# Functions

# Define hotkeys for hotkey listener

# Define quit main loop
def on_activate_q():
    print('<ctrl>+<alt>+q pressed')
    print('program shutting down...')
    sys.exit()

# Define start recording
def on_activate_a():
    print('<alt>+a pressed')
    print('start recording...')
    mouse_start_listening()

# Define stop recording
def on_activate_s():
    print('<alt>+s pressed')
    print('stop recording...')
    # Stop the keyboard listener
    print('listener stopped')
    # Change the mouse listener handle
    set_stop_listening()

# Define play recorded macro
def on_activate_d():
    print('<alt>+d pressed')
    print('play record...')
    play_list()

# Define main program loop
def main_loop():

    # Start hotkey listener
    with keyboard.GlobalHotKeys({
        '<alt>+q': on_activate_q,
        '<alt>+a': on_activate_a,
        '<alt>+s': on_activate_s,
        '<alt>+d': on_activate_d}
        ) as hotkey_listener:
        hotkey_listener.join()
        print_menu()