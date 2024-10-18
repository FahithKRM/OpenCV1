import cv2

image = cv2.imread('C:/Users/FAAHITH KRM/Desktop/OpenCV/OpenCV1/assets/image.png', 1)

## copy && paste the part size of image 
part_image = image[100:400, 0:400] # copy part size of image
image[200:500, 400:800] = part_image # paste the copy part of image paste in different location
## condition must equal  image[100:400, 0:400] == image[200:500, 400:800] (rows, colums) size

cv2.imwrite('OpenCV1/Output/3-copy_paste.png', image)
cv2.imshow('Copy & Paste Image part', image)
cv2.waitKey(0)
cv2.destroyAllWindows()