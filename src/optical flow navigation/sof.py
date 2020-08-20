# Copyright (c) 2020 Yanyu Zhang zhangya@bu.edu All rights reserved.
import numpy as np
import cv2

def sof(video_name, maxCorners=300, maxLevel=2):
    feature_params = dict(maxCorners=maxCorners,
                          qualityLevel=0.3,
                          minDistance=7,
                          blockSize=7)

    lk_params = dict(winSize=(15, 15),
                     maxLevel=maxLevel,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    cap = cv2.VideoCapture(video_name)

    # color = np.random.randint(0, 255, (1000, 3))
    color = (0, 255, 0)

    (ret, old_frame) = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
    mask = np.zeros_like(old_frame)

    # Set the parameter for output
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    sizes = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter('sparse_optical_flow.mp4', fourcc, fps, sizes)

    while True:
        (ret, frame) = cap.read()
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
        # Select good points
        good_old = p0[st == 1]
        good_new = p1[st == 1]

        # mask = np.zeros_like(old_frame)
        
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (a, b), (c, d), color, 2)
            frame = cv2.circle(frame, (a, b), 3, color, -1)
            # frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
        img = cv2.add(frame, mask)

        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

        cv2.imshow('frame', img)
        out.write(img)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    out.release()
    cv2.destroyAllWindows()
    cap.release()