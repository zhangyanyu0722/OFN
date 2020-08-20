# Copyright (c) 2020 Yanyu Zhang zhangya@bu.edu All rights reserved.

# In this code, I will show you how to use dense optical flow to
# detect the features, and calculate the avg_tau to control the motion

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Change the parameters here:
def dof(video_name, split_area = 8, interval = 3, show_flow = True, show_tau = True, show_split = True, show_line = True, norm = False, show_col_flow = False):
    cap = cv2.VideoCapture(video_name)
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    split_w = w/split_area
    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    font=cv2.FONT_HERSHEY_SIMPLEX
    total_tau = [0]*split_area
    avg_tau = [0]*split_area
    font_size = 10/split_area

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    sizes = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    out = cv2.VideoWriter('flow_vector.mp4', fourcc, fps, sizes)
    out2 = cv2.VideoWriter('magnitude_flow_vector.mp4', fourcc, fps, sizes)
    out3 = cv2.VideoWriter('boundary.mp4', fourcc, fps, sizes)
    if show_col_flow:
        plt.ion()
        plt.figure(1)

    while True:
        for i in range(int(interval)):
             ret, frame2 = cap.read()
        frame3 = np.copy(frame2)
        frame4 = np.copy(frame2)
        total_tau = [0]*split_area
        avg_tau = [0]*split_area

        if split_area%2==0:
            for i in range(1, split_area, 1):
                if show_split:
                    cv2.line(frame2, (int(w/split_area*i), 0), (int(w/split_area*i), h), (0, 0, 255), 3)

        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    ##################################################################################
        if norm:
            norm_flow = np.zeros(shape=(int(w/5),int(h/5),2))

            for x in range(0, w, 5):
                for y in range(0, h, 5):
                    for m in range(0, 5, 1):
                        for n in range(0, 5, 1):
                            norm_flow[int(x/5),int(y/5),0] += flow[int(y)+m,int(x)+n,0]
                            norm_flow[int(x/5),int(y/5),1] += flow[int(y)+m,int(x)+n,1]

            norm_flow_dis = np.zeros(shape=(w/5, h/5))

            for i in range(0, 384, 1):
                for j in range(0, 216, 1):
                   norm_flow_dis[i, j] = mean(math.sqrt(norm_flow[i, j, 0]**2 + norm_flow[i, j, 1]**2))
    ##################################################################################      
        flow_dis = np.zeros(shape=(h, w))
        col_flow = []
        for x in range(0, w, 100):
            col_sum = 0
            for y in range(0, h, 100):
                if show_flow:
                    cv2.line(frame2, (int(x), int(y)), (int(x+flow[y, x, 0]), int(y+flow[y, x, 1])), (0, 255, 0), 3)
                if show_tau:
                    if norm:
                        cv2.putText(frame3, '{0:.1f}'.format(abs(norm_flow_dis[int(x/5), int(y/5)])), (x, y), font, 1, (0, 255, 0), 3)
                    else:
                        flow_dis[y, x] = abs(np.sqrt(flow[y, x, 0]**2 + flow[y, x, 1]**2))
                        if show_col_flow:
                            col_sum += flow_dis[y, x]
                        cv2.putText(frame3, '{0:.1f}'.format(flow_dis[y, x]), (x, y), font, 1, (0, 255, 0), 3)
            if show_col_flow:
                col_flow.append(col_sum)
        # Plot the sum of flow vector
        if show_col_flow:
            plt.plot(col_flow)
            plt.title('Magnitude of flow vector in each column')
            plt.show()
            plt.pause(0.02)
            plt.clf()
    ################################################################################## 
        if show_line:
            # up_pos = []
            # down_pos = []
            # left_pos = []
            # right_pos = []
            bf_flow_dis = (abs(flow[:,:,0]) + abs(flow[:,:,0])).T

            for m in range(5, w-5, 5):
                for n in range(5, h-5, 5):
                    if bf_flow_dis[m, n] < 0.1 and bf_flow_dis[m, n+5] > 1:
                        # print(bf_flow_dis[n, m], bf_flow_dis[n+5, m+5])
                        # up_pos.append([m, n])
                        cv2.circle(frame4, (m, n), 3, (0, 255, 0), 3)
                    if bf_flow_dis[m, n] > 1 and bf_flow_dis[m, n+5] < 0.1:
                        # down_pos.append([m, n])
                        cv2.circle(frame4, (m, n), 3, (0, 255, 0), 3)
                    if bf_flow_dis[m, n] > 1 and bf_flow_dis[m+5, n] < 0.01:
                        # left_pos.append([m, n])
                        cv2.circle(frame4, (m, n), 3, (0, 255, 0), 3)
                    if bf_flow_dis[m, n] < 0.01 and bf_flow_dis[m+5, n] > 1:
                        # right_pos.append([m, n])
                        cv2.circle(frame4, (m, n), 3, (0, 255, 0), 3)
                        
    ##################################################################################              
        # o = 0
        # while o < split_area:
        #     m = 0
        #     while m < h:
        #         n = int(split_w*o)
        #         while n < int(split_w*(o+1)):
        #             total_tau[o] += flow[m, n, 1]
        #             n += 1
        #         m += 1
        #     avg_tau[o] = total_tau[o] / (w*h/4)
        #     if show_split:
        #         cv2.putText(frame2, '{0:.1f}'.format(avg_tau[o]*10), (int(split_w/2+split_w*o), int(h/2)), font, 2, (0,0,255), 3)
        #     o += 1
    ##################################################################################
        for o in range(0, split_area, 1):
            for m in range(0, h, 1):
                for n in range(int(split_w*o), int(split_w*(o+1)), 1):
                    total_tau[o] += flow[m, n, 1]
            avg_tau[o] = total_tau[o] / (w*h/4)
            if show_split:
                cv2.putText(frame2, '{0:.1f}'.format(abs(avg_tau[o]*10)), (int(split_w/2+split_w*o-240/split_area), int(h/2)), font, font_size, (0,0,255), 3)

        # print(avg_tau)

        weight_sum = 0
        left_tau = 0
        right_tau = 0

        for r in range(int(split_area/2)):
            if r == int(split_area/2 - 1):
                weight = 1
                left_tau += avg_tau[r]*weight
                right_tau += avg_tau[split_area-r-1]*weight
            else:
                weight = (3)*(split_area/2 - r - 1)
                left_tau += avg_tau[r]*weight
                right_tau += avg_tau[split_area-r-1]*weight
            weight_sum += weight
            # print(left_tau, right_tau, weight)

        left_tau = left_tau / weight_sum
        right_tau = right_tau / weight_sum

        diff = left_tau -right_tau

        if diff <= -2:
            a = "Turn Left"
            color = (0, 0, 255)
        elif diff >= 2:
            a = "Turn Right"
            color = (255, 0, 0)
        else:
            a = "Keep Forward"
            color = (255, 255, 255)

        print(diff, a)

        if show_flow:
            cv2.putText(frame2, '{0:.1f}'.format(diff)+a, (int(w/2)-100, int(h*5/6-25)), font, 1, color, 2, cv2.LINE_AA)
            cv2.imshow('Flow vector', frame2)
            out.write(frame2)
        if show_tau:
            cv2.imshow('Magnitude of flow vector', frame3)
            out2.write(frame3)
        if show_line:
            cv2.imshow('Boundary detection using flow vector', frame4)
            out3.write(frame4)

        cv2.waitKey(1)
        prvs = next
     
    out.release()
    out2.release()
    out3.release()
    cap.release()
    cv2.destroyAllWindows()

