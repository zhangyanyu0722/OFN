# optical-flow-navigation

![Build Status](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8-red)
![Build Status](https://img.shields.io/badge/License-MIT-green)

In terms of [John Baillieul]'s recent research, we developed a new navigation algorithm using [optical flow]. We assume if a vehicle is moving in a straight line and some feature points lie somewhere ahead of the vehicle—possibly to the left or right in the environment, we can calculate the time-to-transit to those features. Then get the mean of time-to-transit in the left half frame and in the right half frame. In the final, we can use a rotation rate(k) to control the rotation.

For more information, [view here].

## Authors
- [John Baillieul] : johnb@bu.edu
- Yanyu Zhang : zhangya@bu.edu
- Feuyang Kang 

## Install
### Requirements
```
python 3.6/3.7/3.8
opencv-contrib-python 4.2.0.32   
opencv-python 4.2.0.32 
numpy 1.18.1 
```
### Quick Install
```
git clone https://github.com/zhangyanyu0722/optical-flow-navigation
```
```
cd optical-flow-navigation
```
```
sudo python setup.py install
```

## Resources

## License
[MIT License]

## Updates
- 4/1/2020 : 

[John Baillieul]:https://www.bu.edu/eng/profile/john-baillieul-ph-d-me-se/
[MIT License]:https://github.com/zhangyanyu0722/optical-flow-navigation/blob/master/LICENSE
[optical flow]:https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html
[view here]:https://github.com/zhangyanyu0722/optical-flow-navigation/blob/master/papers/IFAC-Two-Pixel.pdf
