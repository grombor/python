from pynput.mouse import Controller
from pyautogui import moveTo, click
import time

# The mouse controller
mouse = Controller()

# The list of points
_points_list = []

# Default delay before first action
time_delay = 0.5


# Get the list of the mouse cursor positions
def get_points_list():
    return _points_list


# Set the new position of the mouse cursor
def set_points_list(item):
    _points_list.append(item)


# Print all positions of the mouse cursor
def print_points_list():
    for point in _points_list:
        print(point)


# Click handling function
def click_here(x, y, t):
    time.sleep(t)
    moveTo(x, y, t)
    click()


# Replay mouse behavior from points list
def play_list():
    _points_list
    _time = 0
    for index, point in enumerate(_points_list):
        x = float()
        if index > 0:
            _delay = point.time - _time
            click_here(point.x_pos, point.y_pos, int(_delay))
            _time = point.time
        else:
            click_here(point.x_pos, point.y_pos, time_delay)
            _time = point.time
