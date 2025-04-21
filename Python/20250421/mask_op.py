import cv2

src = cv2.imread(r"Python\20250421\airplane.bmp", cv2.IMREAD_COLOR)
mask = cv2.imread(r"Python\20250421\mask_plane.bmp", cv2.IMREAD_GRAYSCALE)
dst = cv2.imread(r"Python\20250421\field.bmp", cv2.IMREAD_COLOR)

cv2.copyTo(src, mask, dst)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()