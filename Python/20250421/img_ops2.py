import cv2

img1 = cv2.imread(r"Python\20250421\HappyFish.jpg")

img2 = img1  # shallow copy
img3 = img1.copy()  # deep copy

img1.fill(255)

img4 = img3[40:120, 30:150]
img5 = img3[40:120, 30:150].copy()

img4.fill(0)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", img3)
cv2.imshow("img4", img4)
cv2.imshow("img5", img5)
cv2.waitKey()
cv2.destroyAllWindows()
