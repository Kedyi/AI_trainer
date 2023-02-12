# AI_trainer
AI_trainer focuses on counting the number of curls done by an individual.
- It takes the angle formed by the right hand for calculations. 
- We will use the pose estimation running on the CPU to find the correct points and using these points we will get the desired angles. Then based on these angles we can find many gestures including the number of biceps curls
# DEMO

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/93571457/191872646-829c3dae-6b2d-4010-8fb0-821b9ddaf55e.gif)

## Technologies:
![image](https://user-images.githubusercontent.com/93571457/198632307-c5ebcb51-45ca-4ebf-860f-6748f5ec0df6.png)
 ![image](https://user-images.githubusercontent.com/93571457/198631651-b3320f8c-416b-4477-a403-e4830eac663a.png)
 
![image](https://user-images.githubusercontent.com/93571457/198637274-7a7697c3-1840-46c5-9b3f-42383ce08c57.png)

## METHODOLOGY

### - Install and setup 
 _MediaPipe and OpenCV_ :to gather data about the various joints in our body such as our wrists, shoulders, etc. for making our
calculation with angles possible to count our repetitions with heavier weights, _NumPy_ : It will help us with our trigonometry to calculate the angles
### - Make Detections
To make the detections possible, we need to recolor our image because OpenCV renders the RGB image to
BGR color format but for MediaPipe to work, we need to convert our BGR image back to RGB. Print the
detections of our model. Lastly change the color format back to BGR format as OpenCV runs on BGR format, and
then we can start rendering our detections.

### - Determining Joints
There are 33 landmarks in total, starting from index 0. These represent the different joints within the pose, , if
we want to calculate the angle for our Right hand’s bicep curl, we would require the joints of shoulder, elbow and wrist
which are 12, 14 and 16 respectively.

![image](https://user-images.githubusercontent.com/93571457/198642427-f4783e82-e8e5-4958-909b-ebc46a0d1968.png)

### - Calculating Angles 
First we get the coordinates of the threejoints which we require to get the angle calculated. Then we can calculate
the slopes of the joints using NumPy. Angles are calculated in radians which then can be converted into degrees.

## Reference
- https://google.github.io/mediapipe/
- https://google.github.io/mediapipe/solutions/pose.html
- https://github.com/google/mediapipe/tree/master/mediapipe
- http://www.ijaresm.com/ai-personal-trainer-using-opencv-and-python





