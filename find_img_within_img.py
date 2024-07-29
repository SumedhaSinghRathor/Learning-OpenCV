import cv2
import numpy as np

main_image = cv2.imread('renee rapp.png')
template_image = cv2.imread('renee rapp eyes.png')

template_height, template_width, _ = template_image.shape

result = cv2.matchTemplate(main_image, template_image, cv2.TM_CCOEFF_NORMED)

threshold = 0.8
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))

for loc in locations:
    top_left = loc
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
    cv2.rectangle(main_image, top_left, bottom_right, (0, 0, 255), 1)

        
cv2.imshow("Result", main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
