import cv2
import numpy as np

img1 = np.empty((480, 640), dtype=np.uint8)  # grayscale image
img2 = np.zeros((480, 640, 3), dtype=np.uint8)  # truecolor image
img3 = np.ones((480, 640), dtype=np.uint8) * 255  # white image
img4 = np.full((480, 640, 3), (255, 0, 0), dtype=np.uint8)  # BGR image

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.waitKey()
cv2.destroyAllWindows()
