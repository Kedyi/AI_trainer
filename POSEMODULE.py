import cv2
import mediapipe as mp
import time, math

class poseDetector():
    def __init__(self, mode=False, upBody = False, smooth=True,
                 detectionCon = 0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        #model
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(False,False, True, False, False)
        # self.pose = self.mpPose.Pose(self.mode, self.upBody,self.smooth,self.detectionCon,self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        # landmark lists
        self.lm_list=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                  h, w, c = img.shape
                  # print(id, lm)
                  cx , cy = int(lm.x*w), int(lm.y*h)
                  self.lm_list.append([id,cx,cy])
                  if draw:
                     cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
        return self.lm_list

    def findAngle(self, img, p1,p2,p3,draw= True):
        #landmarks
        x1, y1 = self.lm_list[p1][1:]
        x2, y2 = self.lm_list[p2][1:]
        x3, y3 = self.lm_list[p3][1:]

        #get angle
        angle = math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2((y1-y2),(x1-x2)))
        if angle < 0:
            angle+=360
        #print(angle)

     #draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255,255,255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255,255, 255), 3)
            cv2.circle(img, (x1, y2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 5, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 10, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle)),(x2-50,y2+50),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)

        return angle

#testing script
def main():
    cap = cv2.VideoCapture('videos/1.mp4')
    pTime = 0
    detector = poseDetector()
    while (True):
        success, img = cap.read()
        img = cv2.resize(img, (1000, 500))
        img = detector.findPose(img)
        lm_list= detector.findPosition(img,draw=False)
        #print(lm_list[14])
        cv2.circle(img, (lm_list[14][1], lm_list[14][2]), 15, (0, 0, 255), cv2.FILLED)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        cv2.imshow('Image', img)
        cv2.waitKey(10)

if __name__ == "__main__":
   main()