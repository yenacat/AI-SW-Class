import cv2

# import os

# file_list = os.listdir(r"Python\20250421\images")
# img_files = [
#     os.path.join(r"Python\20250421\images", file)
#     for file in file_list
#     if file.endswith((".jpg"))
# ]

import glob

img_files = glob.glob(r"Python\20250421\images\*.jpg")


cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx])

    if img is None:
        print("Image load failed!")
        break

    cv2.imshow("image", img)
    if cv2.waitKey(1000) >= 0:
        break

    idx += 1
    if idx >= cnt:
        idx = 0
