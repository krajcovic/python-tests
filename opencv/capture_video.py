#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

ESC = 27


def capture_video_test():
    cap = cv2.VideoCapture(1)

    for i in range(19):
        print(i, cap.get(i))

    is_video_ok = True

    while cap.isOpened() and is_video_ok:
        # Capture frame-by-frame
        is_video_ok, frame = cap.read()

        if is_video_ok:
            # Our operation on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ESC:
                break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    capture_video_test()
