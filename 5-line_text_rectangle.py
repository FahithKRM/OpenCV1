import cv2

web_camera = cv2.VideoCapture(0)

while True:
    ret, frame = web_camera.read()
    width = int(web_camera.get(3))
    height = int(web_camera.get(4))

    # draw line -> (source_image, start_coor(x,y), end_coor(x,y), BGRvalue(B,G,R), thickness_size)
    draw_image = cv2.line(frame, (width//4, height//4), (width//2, height//2), (0, 255, 0), 5) # first line
    draw_image = cv2.line(draw_image, (width//4, height//2), (width//2, height//4), (0, 255, 0), 5) # second line

    # draw rectange -> (source_image, leftUpCorner(x,y), rightBottomCorner(x,y), BGRvalue(B,G,R), thick_size) thick_size = -1 :: the rectange have filled color
    draw_image = cv2.rectangle(draw_image, (450, 50), (600, 150), (255, 0, 0), 2)

    # draw circle -> (source_image, center(x,y), radiusvalue, BGR, thickness)
    draw_image = cv2.circle(draw_image, (100, 400), 50, (0, 0, 255), -1)

    # draw text -> (source_image, textString, center point, fontType, scale, BGR, lineThickness, lineStyle)
    draw_image = cv2.putText(draw_image, "I'm a winner", (width//3, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (87, 39, 236), 2, cv2.LINE_8)

    cv2.imshow('Draw line, box window', draw_image)
    if cv2.waitKey(1) == ord('q'):
        break

web_camera.release()
cv2.destroyAllWindows()