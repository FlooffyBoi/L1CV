import cv2
filename = 'javaw_KtliLWylWH.png'
image = cv2.imread(filename=filename,flags=cv2.IMREAD_COLOR)
cv2.namedWindow(winname='Display',flags=cv2.WINDOW_NORMAL)
cv2.imshow(winname='Display',mat=image)
cv2.waitKey(0)
cv2.destroyAllWindows()
