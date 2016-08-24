#!/usr/bin/python2
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

ESC = 27


def display_image():
    pressed_key = 0

    img = cv2.imread('rc_zlin_kanec.jpg', cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.putText(img, 'ESC to finish', (1, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow('image', img)

    while pressed_key != ESC:
        pressed_key = cv2.waitKey(0) & 0xFF

        if pressed_key == ESC:
            cv2.destroyAllWindows()
        elif pressed_key == ord('s'):
            cv2.imwrite('kanec_backup.jpg', img)
            print('image saved')
            # cv2.destroyAllWindows()


def display_pyplot_image():
    img = cv2.imread('rc_zlin_kanec.jpg', cv2.IMREAD_ANYCOLOR)
    # b, g, r = cv2.split(img)
    # img2 = cv2.merge([r, g, b])
    img2 = img[:, :, ::-1]# = img[..., ::-1]

    plt.subplot(121);
    plt.imshow(img)  # expects distorted color
    plt.subplot(122);
    plt.imshow(img2)  # expect true color
    plt.show()

    plt.imshow(img2, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    # display_image()
    display_pyplot_image()
