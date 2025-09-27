import cv2
def task5():
    filename = r'input/javaw_KtliLWylWH.png'
    image = cv2.imread(filename,cv2.IMREAD_COLOR)
    hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    cv2.namedWindow("Display",cv2.WINDOW_NORMAL)
    cv2.imshow("Display",image)
    cv2.namedWindow("Display HSV",cv2.WINDOW_NORMAL)
    cv2.imshow("Display HSV",hsv_image)
    cv2.waitKey(0)