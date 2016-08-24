import cv2

ESC = 27

window_name = 'Face detect'


def detect_and_display(frame):
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.equalizeHist(frame_gray, frame_gray)

    # frame_together = cv2.vconcat(frame, frame_gray)
    faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=2,
                                          flags=0 | cv2.cv.CV_HAAR_SCALE_IMAGE, minSize=(30, 30))

    for i in range(len(faces)):
        # cv2.imshow('face', faces[i])
        center = int(round(faces[i][0] + faces[i][2] * 0.5)), int(round(faces[i][1] + faces[i][3] * 0.5))
        axes = int(round(faces[i][2] * 0.5)), int(round(faces[i][3] * 0.5))

        cv2.ellipse(frame,
                    center,
                    axes,
                    0, 0, 360, (0, 0, 0), 2
                    )

        cv2.circle(frame,
                   center=(int(round(faces[i][0] + faces[i][2] * 0.5)), int(round(faces[i][1] + faces[i][3] * 0.5))),
                   radius=2,
                   color=(0, 0, 255))

    cv2.imshow(window_name, frame)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    device_id = 0

    face_cascade_name = '/home/krajcovic/Software/Install-OpenCV/Ubuntu/OpenCV/opencv-2.4.13/data/haarcascades/haarcascade_frontalface_alt.xml'
    eyes_cascade_name = '/home/krajcovic/Software/Install-OpenCV/Ubuntu/OpenCV/opencv-2.4.13/data/haarcascades/haarcascade_eye_tree_eyeglasses.xml'

    face_cascade = cv2.CascadeClassifier()

    # 1. load the cascades
    if not face_cascade.load(face_cascade_name):
        print("Error loading face")
        exit(-1)

    if not cv2.CascadeClassifier().load(eyes_cascade_name):
        print("Error loading eyes")
        exit(-1)

    cap = cv2.VideoCapture(device_id)
    if cap.isOpened():
        while True:
            is_video_ok, frame = cap.read()

            if is_video_ok:
                detect_and_display(frame)
            else:
                print('No captured frame')
                break;

            if cv2.waitKey(1) & 0xFF == ESC:
                break
