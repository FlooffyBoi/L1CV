import cv2
def task9():
    cap = cv2.VideoCapture(r"http://192.168.1.170:8080/video")
    while(cap.isOpened() ):
        ret,frame = cap.read()
        if(frame==None):
            break
        cv2.imshow("IPCAM", cv2.resize(frame,(640,480)))
        if(cv2.waitKey(1)==ord("q")):
            break
    cap.release()