#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

ESC = 27


def capture_video_test(device_id):
    cap = cv2.VideoCapture(device_id)

    for i in range(19):
        try:
            print(i, cap.get(i))
        except:
            pass

    # define the codec and create VideoWriter object
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc=fourcc, fps=20.0, frameSize=(int(cap.get(3)), int(cap.get(4))))

    is_video_ok = True

    while cap.isOpened() and is_video_ok:
        # Capture frame-by-frame
        is_video_ok, frame = cap.read()

        if is_video_ok:
            # Our operation on the frame come here
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            cv2.putText(frame, 'ESC to Finish', (1, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            # todo detect center of head
            cv2.circle(frame, center=(50, 50), radius=20, color=(0, 0, 0))

            out.write(frame)

            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ESC:
                break

    out.release()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    capture_video_test(device_id=0)
