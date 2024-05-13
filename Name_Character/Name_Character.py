import cv2
import numpy as np

img = np.zeros((600,600))

img[20:580,70:150] = 255
img[20:580,450:540] = 255
img[250:350,150:450] = 255 

for i in range(600):
    for j in range(600):
        img[i,j] = 255 - img[i,j]
cv2.imshow('H',img)
cv2.waitKey()
cv2.imwrite('H.jpg',img)