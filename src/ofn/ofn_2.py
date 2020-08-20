# Copyright (c) 2020 Yanyu Zhang zhangya@bu.edu All rights reserved.
import cv2
import numpy as np
# =========================================================================
# =           =           =           =           =           =           =
# =           =           =           =           =           =           =
# =           =           =           =           =           =           =
# =   Left_1  =   Left_2  =   Left_3  =  Right_3  =  Right_2  =  Right_1  =
# =           =           =           =           =           =           =
# =           =           =           =           =           =           =
# =           =           =           =           =           =           =
# =========================================================================

## In this v2, you can choose calculate the featerus in six regions with different weights.
def ofn_2(video_name, feature_num, interval=3, speed=1):
    cap = cv2.VideoCapture(video_name)
    ret, img = cap.read()
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # img = cv2.resize(img, (0,0), fx = 1, fy = 1)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    size = (w, h)
    vout = cv2.VideoWriter()
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    vout.open('output.mp4', fourcc,fps, size, True)
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

        feature = cv2.drawMatches(img1, kps1, img2, kps2, good_matches , img2, flags=2)

        kps1_Left_1 = [] * len(good_matches)
        kps1_Left_2 = [] * len(good_matches)
        kps1_Left_3 = [] * len(good_matches)
        kps1_Right_1 = [] * len(good_matches)
        kps1_Right_2 = [] * len(good_matches)
        kps1_Right_3 = [] * len(good_matches)

        kps2_Left_1 = [] * len(good_matches)
        kps2_Left_2 = [] * len(good_matches)
        kps2_Left_3 = [] * len(good_matches)
        kps2_Right_1 = [] * len(good_matches)
        kps2_Right_2 = [] * len(good_matches)
        kps2_Right_3 = [] * len(good_matches)

        left_points = [] * len(good_matches)
        right_points = [] * len(good_matches)
        good_matches_features_l1 = [] * len(good_matches)
        good_matches_features_l2 = [] * len(good_matches)
        good_matches_features_l3 = [] * len(good_matches)

        for i in range(len(good_matches)):
            if kps2[good_matches[i].trainIdx].pt[0] >= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))*5/6:
                kps1_Right_1.append(kps1[good_matches[i].queryIdx].pt)
                kps2_Right_1.append(kps2[good_matches[i].trainIdx].pt)
                good_matches_features_l1.append(good_matches[i])
            elif kps2[good_matches[i].trainIdx].pt[0] >= (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))*2/3):
                kps1_Right_2.append(kps1[good_matches[i].queryIdx].pt)
                kps2_Right_2.append(kps2[good_matches[i].trainIdx].pt)
                good_matches_features_l2.append(good_matches[i])
            elif kps2[good_matches[i].trainIdx].pt[0] >= (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))*1/2):
                kps1_Right_3.append(kps1[good_matches[i].queryIdx].pt)
                kps2_Right_3.append(kps2[good_matches[i].trainIdx].pt)
                good_matches_features_l3.append(good_matches[i])
            elif kps2[good_matches[i].trainIdx].pt[0] >= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)*1/3):
                kps1_Left_3.append(kps1[good_matches[i].queryIdx].pt)
                kps2_Left_3.append(kps2[good_matches[i].trainIdx].pt)
                good_matches_features_l3.append(good_matches[i])
            elif kps2[good_matches[i].trainIdx].pt[0] >= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)*1/6):
                kps1_Left_2.append(kps1[good_matches[i].queryIdx].pt)
                kps2_Left_2.append(kps2[good_matches[i].trainIdx].pt)
                good_matches_features_l2.append(good_matches[i])
            else:
                kps1_Left_1.append(kps1[good_matches[i].queryIdx].pt)
                kps2_Left_1.append(kps2[good_matches[i].trainIdx].pt)
                good_matches_features_l1.append(good_matches[i])

        Left1_tau_total = 0
        Right1_tau_total = 0
        # if kps1_Left_1 and kps1_Right_1 and region==1:
        if kps1_Left_1 and kps1_Right_1:
            for i in range(len(kps1_Left_1)):
                Left1_tau_total += np.sqrt((kps1_Left_1[i][0]-kps2_Left_1[i][0])**2+(kps1_Left_1[i][1]-kps2_Left_1[i][1])**2)
            Left1_tau_aver = Left1_tau_total / len(kps1_Left_1) / speed

            for j in range(len(kps1_Right_1)):
                Right1_tau_total += np.sqrt((kps1_Right_1[j][0]-kps2_Right_1[j][0])**2+(kps1_Right_1[j][1]-kps2_Right_1[j][1])**2)
            Right1_tau_aver = Right1_tau_total / len(kps1_Right_1) / speed
            # diff = Left1_tau_aver - Right1_tau_aver
            # feature = cv2.drawMatches(img1, kps1, img2, kps2, good_matches_features_l1, None, flags=2)

        Left2_tau_total = 0
        Right2_tau_total = 0
        # if kps1_Left_2 and kps1_Right_2 and region==2:
        if kps1_Left_2 and kps1_Right_2:
            for i in range(len(kps1_Left_2)):
                Left2_tau_total += np.sqrt((kps1_Left_2[i][0]-kps2_Left_2[i][0])**2+(kps1_Left_2[i][1]-kps2_Left_2[i][1])**2)
            Left2_tau_aver = Left2_tau_total / len(kps1_Left_2) / speed

            for j in range(len(kps1_Right_2)):
                Right2_tau_total += np.sqrt((kps1_Right_2[j][0]-kps2_Right_2[j][0])**2+(kps1_Right_2[j][1]-kps2_Right_2[j][1])**2)
            Right2_tau_aver = Right2_tau_total / len(kps1_Right_2) / speed
            # diff = Left2_tau_aver - Right2_tau_aver
            # feature = cv2.drawMatches(img1, kps1, img2, kps2, good_matches_features_l2, None, flags=2)

        Left3_tau_total = 0
        Right3_tau_total = 0
        # if kps1_Left_3 and kps1_Right_3 and region==3:
        if kps1_Left_3 and kps1_Right_3:
            for i in range(len(kps1_Left_3)):
                Left3_tau_total += np.sqrt((kps1_Left_3[i][0]-kps2_Left_3[i][0])**2+(kps1_Left_3[i][1]-kps2_Left_3[i][1])**2)
            Left3_tau_aver = Left3_tau_total / len(kps1_Left_3) / speed

            for j in range(len(kps1_Right_3)):
                Right3_tau_total += np.sqrt((kps1_Right_3[j][0]-kps2_Right_3[j][0])**2+(kps1_Right_3[j][1]-kps2_Right_3[j][1])**2)
            Right3_tau_aver = Right3_tau_total / len(kps1_Right_3) / speed
            # diff = Left3_tau_aver - Right3_tau_aver
            # feature = cv2.drawMatches(img1, kps1, img2, kps2, good_matches_features_l3, None, flags=2)

        Left_tau_aver = (6*Left1_tau_aver + 3*Left2_tau_aver + Left3_tau_aver)/10
        Right_tau_aver = (6*Right1_tau_aver + 3*Right2_tau_aver + Right3_tau_aver)/10

        diff = Left_tau_aver - Right_tau_aver

        if diff >= 50:
            color = (0, 0, 255)
            a = "Turn Left"
        elif diff <= -50:
            color = (255, 0, 0)
            a = "Turn Right"
        else:
            color = (255, 255, 255)
            a = "Keep Forward"

        print(diff, a)
        mask_fig = np.zeros_like(img)
        cv2.putText(mask_fig, '{0:.1f}'.format(diff)+a, (int(w/2)-100, int(h*5/6-25)), font, 1, color, 2, cv2.LINE_AA)

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
