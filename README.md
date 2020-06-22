# Motion Control Using Optical Flow (OFN algorithm)

![Build Status](https://img.shields.io/appveyor/build/gruntjs/grunt)
![Build Status](https://img.shields.io/sonar/test_success_density/swellaby:azure-pipelines-templates?server=https%3A%2F%2Fsonarcloud.io)
![Build Status](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8-red)
![Build Status](https://img.shields.io/badge/License-MIT-green)


[link text](https://youtu.be/nS3XzPC1xZw)


**In terms of [John Baillieul]'s recent research, we developed a new navigation algorithm using [optical flow]. We assume if a vehicle is moving in a straight line and some feature points lie somewhere ahead of the vehicle—possibly to the left or right in the environment, we can calculate the time-to-transit to those features. Then get the mean of time-to-transit in the left half frame and in the right half frame. In the final, we can use a rotation rate(k) to control the rotation.**

**For more information, [view here].**

## Authors
- [John Baillieul] : johnb@bu.edu
- Yanyu Zhang : zhangya@bu.edu
- Feuyang Kang : fykang@bu.edu
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
git clone https://github.com/zhangyanyu0722/optical-flow-navigation
```
```
cd optical-flow-navigation
```
```
sudo python3 setup.py install
```
## Examples
- In the ofn, we use the difference of mean of time-to-transit in the left half frame and in the right half frame to navigation. The use method example is showing in ```ofn_origin.py```.
```
python3 example/ofn_origin.py
```

- In the ofn_v2, we divided the left half frame and the right half frame into three parts, you can choose the parts you want.
The use method example is showing in ```ofn_v2.py```.
```
python3 example/ofn_v2.py
```
## Results
<p align="middle">
  <img src="https://github.com/zhangyanyu0722/optical-flow-navigation/blob/master/images/feature_matching.png">
</p>
<p align="middle">
  <img src="https://github.com/zhangyanyu0722/optical-flow-navigation/blob/master/images/navigation.png" height="300" width="1000"> 
</p>

## Resources
- https://www.bu.edu/eng/profile/john-baillieul-ph-d-me-se/
- https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html
- https://docs.opencv.org/3.4/db/d39/classcv_1_1DescriptorMatcher.html
- https://docs.opencv.org/3.4/d3/da1/classcv_1_1BFMatcher.html

## License
[MIT License]

## Updates
- 4/12/2020 : Update ofn and ofn_v2 

[John Baillieul]:https://www.bu.edu/eng/profile/john-baillieul-ph-d-me-se/
[MIT License]:https://github.com/zhangyanyu0722/optical-flow-navigation/blob/master/LICENSE
[optical flow]:https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html
[view here]:https://github.com/zhangyanyu0722/optical-flow-navigation/blob/master/papers/IFAC-Two-Pixel.pdf





