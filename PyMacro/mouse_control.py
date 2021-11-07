from time import time
from pynput import mouse
from pointer import Pointer
from points_list import set_points_list

# Global mouse listener handle; if True, will stop mouse listener
_stop_listening = False


# Function to change state of mouse listener
def set_stop_listening():
    global _stop_listening
    if _stop_listening:
        _stop_listening = False
    else:
        _stop_listening = True


def on_move(x, y):
    # If global mouse listener handle is True, it will shutdown mouse listener
    if _stop_listening:
        print("mouse listening stopped")
        return False


def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
    else:
        # print('Mouse released at ({0}, {1}) with {2}'.format(x, y, button))
        create_point(x, y)


# Create and add a record (x,y position of the cursor, and timestamp) to points_list
def create_point(x, y):
    p = Pointer(x, y, time())
    set_points_list(p)
    # print_points_list()


# Start mouse listening
def mouse_start_listening():
    listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        # on_scroll=on_scroll
    )
    listener.start()
