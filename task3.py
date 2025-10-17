import cv2
import time

def task3():
    cap_properties = [[],
                      [(cv2.CAP_PROP_MONOCHROME,1)],
                      [(cv2.CAP_PROP_FRAME_WIDTH,400),(cv2.CAP_PROP_FRAME_HEIGHT,800)]]
    filename = r'input/video1.mp4'
    for prop in cap_properties:
        
        if len(prop)==0:
            cap = cv2.VideoCapture(filename,cv2.CAP_ANY)
        else:
            cap = cv2.VideoCapture(filename,cv2.CAP_ANY)
            for p,v in prop:
                cap.set(p,v) # не работает :(
        cv2.namedWindow("Video capture",cv2.WINDOW_AUTOSIZE)
        fps = cap.get(cv2.CAP_PROP_FPS)
        spf = 1/fps
        video_start = time.time()
        while(True):
            frame_start = time.time()
            ret,frame = cap.read()        
            if not(ret):
                break
            cv2.imshow('Video capture',frame)
            delta = time.time() - frame_start
            if spf-delta>0:
                time.sleep(spf - delta)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        video_end = time.time()
        print(video_end-video_start)
        cap.release()
        cv2.destroyAllWindows()
    
