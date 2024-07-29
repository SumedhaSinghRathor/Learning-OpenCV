import numpy as np
import cv2

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

def tracker_callback(x):
    pass

cv2.createTrackbar('R', 'image', 0, 255, tracker_callback)
cv2.createTrackbar('G', 'image', 0, 255, tracker_callback)
cv2.createTrackbar('B', 'image', 0, 255, tracker_callback)

while True:
    cv2.imshow('image', img)

    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')

    img[:] = [b, g, r]

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()
