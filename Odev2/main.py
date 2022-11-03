import cv2
import numpy as np

img = cv2.imread("resimler/kedi.jpg",0)
cv2.imshow("Test2",img)
inverted = np.invert(img)
[w,h] = (img.shape)
max = (np.max(img))
img2 = np.zeros([w,h], dtype=np.uint8)
for v in range(0,w):
    for u in range(0,h):
        img2[v,u] = max - img[v,u]
cv2.imshow("test",img2)
cv2.waitKey(0)