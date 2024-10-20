import cv2

image = cv2.imread('assets/image.jpg', 1)

image = cv2.resize(image, (0, 0), fx=0.75, fy=0.75)
## copy && paste the part size of image 
part_image = image[100:300, 100:400] # copy part size of image
image[0:200, 200:500] = part_image # paste the copy part of image paste in different location
## condition must equal  image[100:300, 100:400] == image[0:200, 200:500] (rows, colums) size

cv2.imwrite('Outputs/3-copy_paste.png', image)
cv2.imshow('Copy & Paste Image part', image)
cv2.waitKey(0)
cv2.destroyAllWindows()