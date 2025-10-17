import cv2
import math
"""
def drawCallback(callbackStack,frame):
    if(callbackStack!=[]):
        func, *params = callbackStack[-1]
        if(len(params)<2):
            return frame
        if(func==cv2.rectangle):
            newFrame = func(frame,params[0],params[1],(0,0,255),4,cv2.LINE_8)
            return drawCallback(callbackStack[:-1],newFrame)
        if(func==cv2.blur):
            x1,y1 = params[0]
            x2,y2 = params[1]
            roi = frame[y1:y1+y2, x1:x1+x2]
            kernelSize = (5,5)
            blurred_roi = cv2.blur(roi,kernelSize)
            newFrame=frame
            newFrame[y1:y1+y2, x1:x1+x2]=blurred_roi
            return drawCallback(callbackStack[:-1],newFrame)
    else:
        return frame
"""
def task6():
    """
    callbackStack = []
    def mouseRect(event,x,y,flags,param):
        if(event == cv2.EVENT_LBUTTONDOWN):
            callbackStack.append([cv2.rectangle])
            callbackStack[-1].append((x,y))
            return
        if(event==cv2.EVENT_LBUTTONUP):
            callbackStack[-1].append((x,y))
            
            return
        if(event==cv2.EVENT_RBUTTONDOWN):
            callbackStack.append([cv2.blur])
            callbackStack[-1].append((x,y))
            return
        if(event==cv2.EVENT_RBUTTONUP):
            callbackStack[-1].append((x,y))
            x1,y1 = callbackStack[-1][1]
            x2,y2 = callbackStack[-1][2]
            if(x1>x2):
                buf = x1
                x1 = x2
                x2 = buf
            if(y1>y2):
                buf = y1
                y1 = y2
                y2 = buf
            if(x2>639):
                x2=639
            if(y2>479):
                y2=479
            if(x1<0):
                x1=0
            if(y1<0):
                y1=0
            callbackStack[-1][1] = (x1,y1)
            callbackStack[-1][2] = (x2,y2)
            return
    """
    cv2.namedWindow("frame",cv2.WINDOW_AUTOSIZE)
    #cv2.setMouseCallback("frame",mouseRect)

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

        kernelsize = (25,25)
    
        roi = frame[rect2ay:rect2by, rect2ax:rect2bx]
        blurred_roi = cv2.blur(roi,kernelsize)
        frame[rect2ay:rect2by, rect2ax:rect2bx] = blurred_roi

        cv2.rectangle(frame,(rect2ax,rect2ay),(rect2bx,rect2by),(0,0,255),4,cv2.LINE_8)
        cv2.rectangle(frame,(rect1ax,rect1ay),(rect1bx,rect2ay),(0,0,255),4,cv2.LINE_8)
        cv2.rectangle(frame,(rect1ax,rect1by),(rect1bx,rect2by),(0,0,255),4,cv2.LINE_8)
        
        cv2.imshow("frame",frame)
        if(cv2.waitKey(1)==ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()