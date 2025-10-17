import cv2
import time
import math
def task7():
    filename = r"output/task7out.mp4"
    cap = cv2.VideoCapture(0,cv2.CAP_ANY)
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    out = cv2.VideoWriter(filename,codec,fps,(width,height))
    cv2.namedWindow("frame",cv2.WINDOW_AUTOSIZE)
    timeStart = time.time()
    while cap.isOpened() and time.time()-timeStart<5:
        ret,frame = cap.read()
        if not ret:
            break
        cv2.imshow("frame",frame)
        out.write(frame)
        time.sleep(1/fps-0.001)
        cv2.waitKey(1)
        
    cap.release()
    out.release()