from sre_constants import SUCCESS
import cv2
import mediapipe as mp 
import time 

cap = cv2.VideoCapture("S2.mp4")
ptime = 0

mpFaceMesh = mp.solutions.face_mesh
mpDraw = mp.solutions.drawing_utils
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2 )
drawspec = 
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    if results.multi_face_landmarks:
       for facelms in results.multi_face_landmarks:
           mpDraw.draw_landmarks(img, facelms, mpFaceMesh.FACE_CONNECTIONS)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img,f'FPS:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)       
    cv2.imshow("Image",img)
    cv2.waitKey(10)

