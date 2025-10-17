import cv2
import math

def closestRGB(p):
    #BGR
    distR = math.dist(p,[0,0,1])
    distG = math.dist(p,[0,1,0])
    distB = math.dist(p,[1,0,0])
    if(distR>=distG and distR>=distB):
        return (0,0,255)
    if(distG>=distR and distG>=distB):
        return (0,255,0)
    else:
        return (255,0,0)

def task8():
    cv2.namedWindow("frame",cv2.WINDOW_AUTOSIZE)
    filename = r'input/javaw_KtliLWylWH.png'
    cap = cv2.VideoCapture(0)
    while(True):
        ret, frame = cap.read()
        if(not ret):
            print("Cannot retreive frame")
            break

        sizeY,sizeX,*_ = frame.shape

        rect1ax = math.floor(sizeX*(0.5-0.0375))
        rect1bx = math.floor(sizeX*(0.5+0.0375))
        rect1ay = math.floor(sizeY*(0.5-0.2))
        rect1by = math.floor(sizeY*(0.5+0.2))

        rect2ax = math.floor(sizeX*(0.5-0.125))
        rect2bx = math.floor(sizeX*(0.5+0.125))
        rect2ay = math.floor(sizeY*(0.5-0.05))
        rect2by = math.floor(sizeY*(0.5+0.05))

        c1X = round((rect2ax+rect2bx)/2)
        c1Y = round((rect2ay+rect2by)/2)
        col1 = closestRGB(frame[c1Y,c1X])
        cv2.rectangle(frame,(rect2ax,rect2ay),(rect2bx,rect2by),col1,cv2.FILLED)
        cv2.rectangle(frame,(rect2ax,rect2ay),(rect2bx,rect2by),(0,0,255),4,cv2.LINE_8)

        c2X = round((rect1ax+rect1bx)/2)
        c2Y = round((rect1ay+rect2ay)/2)
        col2 = closestRGB(frame[c2Y,c2X])
        cv2.rectangle(frame,(rect1ax,rect1ay),(rect1bx,rect2ay),col2,-1)
        cv2.rectangle(frame,(rect1ax,rect1ay),(rect1bx,rect2ay),(0,0,255),4,cv2.LINE_8)

        c3X = round((rect1ax+rect1bx)/2)
        c3Y = round((rect2by+rect1by)/2)
        col3 = closestRGB(frame[c3Y,c3X])
        cv2.rectangle(frame,(rect1ax,rect2by),(rect1bx,rect1by),col3,-1)
        cv2.rectangle(frame,(rect1ax,rect2by),(rect1bx,rect1by),(0,0,255),4,cv2.LINE_8)
        
        cv2.imshow("frame",frame)
        if(cv2.waitKey(1)==ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()