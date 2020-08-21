# Motion Control using Optical Flow (OFN)

![Build Status](https://img.shields.io/appveyor/build/gruntjs/grunt)
![Build Status](https://img.shields.io/sonar/test_success_density/swellaby:azure-pipelines-templates?server=https%3A%2F%2Fsonarcloud.io)
![Build Status](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8-red)
![Build Status](https://img.shields.io/badge/License-MIT-green)

**This respository develops two algorithms to control the motion of vehicles using [optical flow], which can detect the surrounding world frame by frame. The first algorithm is through tracking features in continuously updated sequences of frames using sparse optical flow, and using these feature tracks to calculate time-to-transit (τ) for the matched features as a feedback signal. Such signals can steer the robot vehicle by balancing average of τ in certain areas. The second algorithm uses dense optical flow by calculating the difference of flow vectors in two regions in one frame to generate a steering signal to control the robot.**

## Authors
- Yanyu Zhang : zhangya@bu.edu
- John Baillieul : johnb@bu.edu
- *The authors are with the Departments of Mechanical Engineering, Electrical and Computer Engineering, and the Division of Systems Engineering at Boston University, Boston, MA 02115.*

## Install
### Requirements
```
python==3.6/3.7/3.8
opencv-contrib-python==4.2.0.32   
opencv-python==4.2.0.32 
numpy==1.18.1 
```
### Quick Install
```
git clone https://github.com/zhangyanyu0722/OFN
```
```
cd OFN
```
```
sudo python3 setup.py install
```
## Examples
- In the ```example/ofn_test.py```, there are four testing example for these two algorithms. In order to run the code, you need to uncommend anyone of them.

### Test optical flow navigation with two split areas or six slipt areas, you need to uncommand the ```ofn``` and ```ofn_2``` section.

<p align="middle">
  <img src="https://github.com/zhangyanyu0722/OFN/blob/master/images/ofn.gif"> 
</p>

### Test the sparse optical flow: you need to uncommand the ```sof``` section.

<p align="middle">
  <img src="https://github.com/zhangyanyu0722/OFN/blob/master/images/sof.gif">
</p>

### Test the dense optical flow: you need to uncommand the ```dof``` section.

<p align="middle">
  <img src="https://github.com/zhangyanyu0722/OFN/blob/master/images/boundary.gif">
  <img src="https://github.com/zhangyanyu0722/OFN/blob/master/images/magnitude_flow.gif">
</p>

## Resources
- https://www.bu.edu/eng/profile/john-baillieul-ph-d-me-se/
- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html
- https://docs.opencv.org/3.4/db/d39/classcv_1_1DescriptorMatcher.html
- https://docs.opencv.org/3.4/d3/da1/classcv_1_1BFMatcher.html

## License
[MIT License]

[MIT License]:https://github.com/zhangyanyu0722/optical-flow-navigation/blob/master/LICENSE
[optical flow]:https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html






