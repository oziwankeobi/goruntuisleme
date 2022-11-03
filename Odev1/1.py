import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("resimler/deneme2.jpg",0)
cv2.imshow("Test",img)
z = np.zeros(256)
[w,h] =(img.shape)
for v in range(0,w):
    for u in range(0,h):
        i = img[v, u]
        z[i] = z[i]+1
for v in range(0,255):
    print("{}-{}".format(v,z[v]))
plt.style.use("fivethirtyeight")
plt.hist(z)
plt.show()