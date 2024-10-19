import cv2
import numpy as np

web_camera = cv2.VideoCapture(0)

while True:
    ret, frame = web_camera.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# Always use HSV for setting color ranges when performing 
# color detection or segmentation in OpenCV, as it simplifies 
# isolating colors and is more reliable under different lighting conditions.

    # set the hsv value color range for blue color detection
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # set range hsv value for green color detection
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])

    # range hsv value for lower red
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])

    # range hsv value for upper red
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    # mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    # mask = cv2.inRange(hsv_image, lower_green, upper_green)
    mask = cv2.inRange(hsv_image, lower_red2, upper_red2)        
     # fall in the range binary value = 1 othervise value = 0

    result = cv2.bitwise_and(frame, frame, mask=mask) # 0 -> black, 1 -> white

    cv2.imshow("Color Detection Window", hsv_image)
    cv2.imshow("Blue Color Detection Window", result)
    cv2.imshow("AND boolean Detection Window", mask) # 0 -> black, 1 -> white

    if cv2.waitKey(1) == ord('q'):
        break

web_camera.release()
cv2.destroyAllWindows( )

# When working with OpenCV for color detection, it is generally 
# better to use the HSV color space rather than the BGR color space. 

# 1. Why HSV?
# The HSV (Hue, Saturation, Value) color space is more effective 
# for color-based tasks like detection, segmentation, and tracking for the following reasons:

# Hue (H): Defines the color type (e.g., blue, red, green). This makes it easier to isolate a particular color range, independent of brightness.
# Saturation (S): Describes the intensity of the color (from faded to fully saturated). By specifying a range for saturation, you can exclude very light colors.
# Value (V): Refers to the brightness of the color. You can control brightness, helping to ignore shadows or overexposed areas.
# In the HSV model, colors are more perceptually uniform and easier to isolate, especially in real-world environments where lighting can vary.

# 2. Why Not BGR?
# BGR (or RGB) color spaces are less intuitive when isolating specific colors. 
# This is because the color components (blue, green, red) are highly correlated 
# with light intensity and often don't form distinct ranges for particular colors. 
# Detecting colors directly in BGR may lead to incorrect or inconsistent results, 
# especially under changing lighting conditions.