# Copyright (c) 2020 Yanyu Zhang zhangya@bu.edu All rights reserved.
import cv2
import numpy as np

def ofn(video_name, feature_num, interval, speed=1):
    cap = cv2.VideoCapture(video_name)
    ret, img = cap.read()
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # img = cv2.resize(img, (0,0), fx = 1, fy = 1)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    vout = cv2.VideoWriter()
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    vout.open('output.mp4', fourcc,fps, (w, h), True)
    img1 = img

    font = cv2.FONT_HERSHEY_SIMPLEX

    while 1:
        for i in range(int(interval)):
            ret, img2 = cap.read()

        if img1 is None or img2 is None:
            print('Could not open or find the images!')
            break

        orb = cv2.ORB_create(nfeatures = 1000,   # 1000
            scaleFactor = 1.2,
            scoreType = cv2.ORB_HARRIS_SCORE)  # FAST_SCORE

        kps1, des1 = orb.detectAndCompute(img1, None)
        kps2, des2 = orb.detectAndCompute(img2, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
        # matches = bf.knnMatch(des1, des2, k=1)
        matches = bf.match(des1,des2)
        matches = sorted(matches, key = lambda x : x.distance)
        good_matches = matches[:feature_num]
        
        # Show difference between Hamming distance and Euler distance
        # print(good_matches[i].distance)
        # print(kps1[good_matches[i].queryIdx].pt, kps2[good_matches[i].trainIdx].pt)
        # print(np.sqrt((kps1[good_matches[i].queryIdx].pt[0]-kps2[good_matches[i].trainIdx].pt[0])**2+(kps1[good_matches[i].queryIdx].pt[1]-kps2[good_matches[i].trainIdx].pt[1])**2))

        feature = cv2.drawMatches(img1, kps1, img2, kps2, good_matches , img2, flags=2)
        # index = [[]for i in range(len(good_matches))]

        ##############################################################################
        # # Hamming Distance
        # left_tau = [] * len(good_matches)
        # right_tau = [] * len(good_matches)

        # for i in range(len(good_matches)):
        #     if kps2[good_matches[i].queryIdx].pt[0] >= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2):
        #         right_tau.append(good_matches[i].distance)
        #     else:
        #         left_tau.append(good_matches[i].distance)

        # diff = np.mean(left_tau) - np.mean(right_tau)
        ##############################################################################
        # Euler Distance
        kps1_left_points = [] * len(good_matches)
        kps1_right_points = [] * len(good_matches)
        kps2_left_points = [] * len(good_matches)
        kps2_right_points = [] * len(good_matches)

        for i in range(len(good_matches)):
            # index[i].append(good_matches[i].queryIdx)
            # index[i].append(good_matches[i].trainIdx)
            # index[i].append(kps1[good_matches[i].queryIdx].pt)
            # index[i].append(kps2[good_matches[i].trainIdx].pt)
            # index[i].append(good_matches[i].distance)
            if kps2[good_matches[i].queryIdx].pt[0] >= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)/2):
                kps1_right_points.append(kps1[good_matches[i].queryIdx].pt)
                kps2_right_points.append(kps2[good_matches[i].trainIdx].pt)
            else:
                kps1_left_points.append(kps1[good_matches[i].queryIdx].pt)
                kps2_left_points.append(kps2[good_matches[i].trainIdx].pt)
        
        left_tau_total = 0
        for i in range(len(kps1_left_points)):
            left_tau_total += np.sqrt((kps1_left_points[i][0]-kps2_left_points[i][0])**2+(kps1_left_points[i][1]-kps2_left_points[i][1])**2)
        left_tau_aver = left_tau_total / len(kps1_left_points) / speed

        right_tau_total = 0
        for j in range(len(kps1_right_points)):
            right_tau_total += np.sqrt((kps1_right_points[j][0]-kps2_right_points[j][0])**2+(kps1_right_points[j][1]-kps2_right_points[j][1])**2)
        right_tau_aver = right_tau_total / len(kps1_right_points) / speed
      
        diff = left_tau_aver - right_tau_aver
        ##############################################################################
        if diff >= 50:
            color = (0, 0, 255)
            movement = "Turn Left"
        elif diff <= -50:
            color = (255, 0, 0)
            movement = "Turn Right"
        else:
            color = (255, 255, 255)
            movement = "Keep Forward"

        print(diff, movement)
        mask_fig = np.zeros_like(img)
        cv2.putText(mask_fig, '{0:.1f}'.format(diff)+movement, (int(w/2)-100, int(h*5/6-25)), font, 1, color, 2, cv2.LINE_AA)

        split_area = 6
        for i in range(1, split_area, 1):
            cv2.line(mask_fig, (int(w/split_area*i), 0), (int(w/split_area*i), h), (0, 0, 255), 3)

        img = cv2.add(img2, mask_fig)
        vout.write(img)
        img1 = img2

        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('Image', w, h)
        cv2.imshow('Image', img)
        cv2.imshow('Feature_track', feature)

        cv2.waitKey(1)