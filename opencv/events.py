import cv2
import numpy as np
from enum import *

# if mouse is pressed
drawing = False


# draw rectangel. Press 'm' to toggle to cureve
# class Modes(Enum):
#     rectange = 1
#     circle = 2

Modes = Enum('rectange', 'circle', 'max')

mode = Modes.rectange


RunningStates = Enum('idle', 'cont', 'exit')

ix, iy = -1, -1


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == Modes.rectange:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)

            if mode == Modes.circle:
                cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    if event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == Modes.rectange:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 1)

        if mode == Modes.circle:
            cv2.circle(img, (x, y), 5, (0, 0, 255), 1)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), 1)


def get_mouse_events():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    return events


def check_key():
    global mode

    pressed_key = cv2.waitKey(1) & 0xFF

    if pressed_key == ord('m'):
        if mode == Modes[Modes.max.index - 1]:
            mode = Modes[0]
        else:
            mode = Modes[mode.index + 1]

        return RunningStates.cont

    if pressed_key == 27:
        return RunningStates.exit


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)

    if check_key() == RunningStates.exit:
        break

cv2.destroyAllWindows()
