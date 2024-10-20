import cv2

image = cv2.imread('assets/image.jpg', 1)

# cv2.IMREAD_COLOR (default): Loads a color image. Any transparency of the image will be neglected. 
# It is the default flag, so if you don't specify the second argument, the image will be read as a color image.
# Value: 1

# cv2.IMREAD_GRAYSCALE: Loads the image as a grayscale image (black and white).
# Value: 0

# cv2.IMREAD_UNCHANGED: Loads the image, including any alpha channel (transparency).
# Value: -1

image = cv2.resize(image, (0, 0), fx=0.75, fy=0.75)
image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('Outputs/1-basic_operation.png', image)
cv2.imshow('Image Window', image) # set the window name
cv2.waitKey(0) # 0 means destroy infinity times press any key destroy the window othervise
                # put as (5) after 5 second press any key automatically destroy the window
cv2.destroyAllWindows()