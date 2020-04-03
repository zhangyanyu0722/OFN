from optical_flow_navigation import ofn_v2

video_name = 'test.mov'
interval=3
mov_speed=2
region=2

ofn_v2(video_name=video_name, 
       interval=interval, 
       speed=mov_speed, 
       region=region)