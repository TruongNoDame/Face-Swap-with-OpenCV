# Face swap with OpenCV

This is a small project aim to implemet a swapping faces method, in which we use module dlib landmark detection.

## Installation and setup
### 1. Installation & setup
**I recommend you use python 3.7, 3.8 or 3.9.**

##### 1.1 With conda
`bash run/setup_conda.sh`

##### 1.2 With virtualenv
After you create an enviroment by using `virtualenv`. You have to remove line `dlib==19.22.99` in `requirements.txt`. Then run command bellow in virtualenv enviroment.

`bash run/setup_no_conda.sh`

Note: that to download dlib for python when not using conda you need to follow these instructions:

First: following [this solution](https://github.com/sachadee/Dlib), you need to see [this issue](https://github.com/sachadee/Dlib/issues/2#issue-1862541044) before running

### 2. Install model for dlib
You need put model file weights in folder models by **downloading the shape-predictor-68-face-landmarks.dat [here](https://drive.google.com/file/d/1ysJAViqMnkVhp2Bt2pMgIYC83WsSyg71/view?usp=sharing)**

## Usae
### 1. Face swapping picture to picture
+ To use this function, you need at least 2 pictures, each contains only 1 face.
+ Put your pictures into the 'images' folder to use them.
```
python utils/face_swap_picture.py --source_image_name=<SOURCE_IMAGE_NAME> --des_image_name=<DES_IMAGE_NAME>
```

In this:
+ source_image_name: the name of picture you take the face from(E.g. Mickey.png)
+ des_image_name: the name of picture you stick the face into(E.g. Donald.jpg)

### 2. Face swapping real-time with camera
+ To use this function, you need at least 1 picture which contains only 1 face.
+ A webcam(of course)
+ Run the command below:
```
python utils/face_swap_realtime.py --image_name=<IMAGE_NAME> --video_name=<VIDEO_NAME> 
```

In this:
+ image_name: the name of picture you take the face from(E.g. Jack.png)
+ video_name: the name you choose for the output video file (E.g. Funny_face_swaping_clip)

**The loop would run until you press the key 'p'**
