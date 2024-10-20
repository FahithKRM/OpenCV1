import numpy as np
import cv2

image = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.5, fy=0.5)
template = cv2.resize(cv2.imread('assets/ball.PNG', 0), (0, 0), fx=0.5, fy=0.5)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    image2 = image.copy()

    result = cv2.matchTemplate(image2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)    
    cv2.rectangle(image2, location, bottom_right, 255, 5)
    cv2.imshow('Template Maching Window', image2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()