import cv2
def task4():
    filename = r'input/video1.mp4'
    cap = cv2.VideoCapture(filename,cv2.CAP_ANY)
    codec = cv2.VideoWriter_fourcc(*'mp4v')
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    out = cv2.VideoWriter('output/output.mp4',codec,24,(width,height))
    
    while cap.isOpened():
        ret,frame = cap.read()
        if not ret:
            break
        out.write(frame)
    cap.release()
    out.release()