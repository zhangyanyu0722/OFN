# Copyright (c) 2020 Yanyu Zhang zhangya@bu.edu All rights reserved.
from optical flow navigation import ofn, ofn_2, dof, sof
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Test optical flow navigation with two split areas
ofn(video_name='test.mov',  # The address of video
	feature_num=500,  # Feature density : 0 ~ 500
	interval=1,   # Frame interval : >=1 (recommend not too big)
	speed=1)  # Robot line speed : >= 0
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Test optical flow navigation with six split areas
ofn_2(video_name='test.mov',  # The address of video
	feature_num=500,  # Feature density : 0 ~ 500
	interval=1,   # Frame interval : >=1 (recommend not too big)
	speed=1)  # Robot line speed : >= 0
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Test sparse optical flow
sof(video_name='test.mov',  # The address of video
	maxCorners=100,   # Feature density : >= 0 (recommend 50 ~ 500)
	maxLevel=2)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Test dense optical flow with magnitudes of the flow vectors
dof(video_name='test.mov',  # The address of video
	split_area = 6,  # The splited areas used to calcalte tau in each reagon
	                 # must be even number, (recommend 2, 4, 6, 8)
	interval = 1,  # Frame interval : >=1 (recommend not too big)
    # -------------------------------------------------------------------------
	# Other function that can be choose here : 
	# (Warning: donot recommend to initial all functions below)
	show_flow = True,  # Show flow vector and saved as a video
	show_tau = False,  # Show the magnitude of flow vector and saved as a video
	show_split = False,  # Show the splited line of reagons in the flow vector
	                     # initial the "show_flow = T" before using it.
	show_line = False,  # Show the boundary of walls based on flow vector.
	norm = False,  # Using normalization to each pixel. (recommend using False)
	show_col_flow = False)  #  Show the sum of flow vector in each column.)
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------