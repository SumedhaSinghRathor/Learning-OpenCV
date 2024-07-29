import cv2

def get_pixel_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        bgr_color = img[y, x]
        print('BGR color: ', bgr_color)
        rgb_color = tuple(reversed(bgr_color))
        print('RGB color: ', rgb_color)

img = cv2.imread('chappell roan.png')
cv2.namedWindow('image')
cv2.setMouseCallback('image', get_pixel_color)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
