import cv2

img1 = cv2.imread(r"Python\20250421\cat.bmp", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r"Python\20250421\cat.bmp", cv2.IMREAD_COLOR)

print(f"type(img1): {type(img1)}")
print(f"type(img2): {type(img2)}")

print(
    f"img1 ndim: {img1.ndim}, shape: {img1.shape}, size: {img1.size}, dtype: {img1.dtype}"
)
print(
    f"img2 ndim: {img2.ndim}, shape: {img2.shape}, size: {img2.size}, dtype: {img2.dtype}"
)


h, w = img1.shape[:2]  # height = 480, width = 640
print(f"img2 size: {w} x {h}")


if len(img1.shape) == 2:
    print("img1 is grayscale image")
elif len(img1.shape) == 3:
    print("img1 is truecolor image")

for y in range(h):
    for x in range(w):
        img1[y, x] = 255
        img2[y, x] = [0, 255, 122]  # BGR

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
