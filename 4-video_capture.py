import numpy as np
import cv2

video_cap = cv2.VideoCapture(0) # (value) -> 0, 1, 2, -->> means : web camera state
        # 0 -> 1st web camera, 1 -> 2nd web camera, 2 -> 3rd web camera, ...

while True:
    ret, frame = video_cap.read() # ret -> boolean var frame successfully read or not
    height = int(video_cap.get(4)) # get the camera frame height
    width = int(video_cap.get(3))  # get the camera frame weight

    image = np.zeros(frame.shape, np.uint8) # create the blank image same size of the frame
        # np.zeros -> an array filled with zeros 
        # np.unit8 -> unsigned 8-bit intiger pixel range [0, 255]

    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # change the image size
    # same image in multiple times (resize) can also apply the rotation apply for first frame
    image[:height//2, :width//2] = smaller_frame # position : left-top
    image[height//2:, :width//2] = smaller_frame # position : left-bottom
    image[:height//2, width//2:] = smaller_frame # position : right-top
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) # position : right-bottom

    cv2.imshow('Web Camera Frame', image ) # display the frame
    if cv2.waitKey(1) == ord('q'): 
        break

video_cap.release()
cv2.destroyAllWindows()