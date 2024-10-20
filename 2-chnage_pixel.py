import cv2
import random

image = cv2.imread('assets/image.jpg', 1)
# print(image) # print the image pixel in numpy array
# print(type(image)) # pixel type = numpy
# print(image.shape) # (rows, columns, channel) -> channel is BGR ->> (Standard is RGB but in OpenCV BGR)

## change the pixel color in image
for i in range(100): # set row size 
    for j in range(image.shape[1]): # shape[0] -> represent row & shape[1] -> represent columns
        image[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imwrite('Outputs/2-chnage_pixel.png', image)
cv2.imshow('Change Image Pixel', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
