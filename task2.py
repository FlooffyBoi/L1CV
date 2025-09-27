import cv2

def task2():
    filename = r'input/javaw_KtliLWylWH.png'
    image_color = cv2.imread(filename=filename,flags=cv2.IMREAD_COLOR)
    image_grayscale = cv2.imread(filename=filename,flags=cv2.IMREAD_GRAYSCALE)
    image_reduced_color = cv2.imread(filename=filename,flags=cv2.IMREAD_REDUCED_COLOR_2)
    cv2.namedWindow(winname='Display',flags=cv2.WINDOW_NORMAL)
    cv2.imshow(winname='Display',mat=image_color)
    cv2.namedWindow(winname='Display Autosize',flags=cv2.WINDOW_AUTOSIZE)
    cv2.imshow(winname='Display Autosize',mat=image_grayscale)
    cv2.namedWindow(winname='Display Expanded',flags=cv2.WINDOW_GUI_EXPANDED)
    cv2.imshow(winname='Display Expanded',mat=image_reduced_color)
    cv2.destroyAllWindows()