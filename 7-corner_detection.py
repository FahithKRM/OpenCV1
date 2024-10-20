import cv2
import numpy as np
import random

image = cv2.imread('assets/image.jpg')
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5) # it's not compalasry
# corner detection algorithm "Shi-Tomasi" only work on gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# algorithm (source_image, no.of corners, minimum-quality, min-euclidean-distance)
corners = cv2.goodFeaturesToTrack(gray_image, 100, 0.01, 10)
corners = np.int_(corners)

# draw circle
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 5, (0, 0, 255), 2) 

cv2.imwrite('Outputs/7-corner_detection1.png', image) 

# draw line
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x : int(x), np.random.randint(0, 255, size=3)))
        cv2.line(image, corner1, corner2, color, 1)

cv2.imwrite('Outputs/7-corner_detection2.png', image) 

cv2.imshow("Corner Detection Window", image)
cv2.waitKey(0)
cv2.destroyAllWindows()