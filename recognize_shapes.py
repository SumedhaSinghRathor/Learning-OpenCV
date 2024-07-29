import cv2
import numpy as np

img = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    perimeter = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)
    num_vertices = len(approx)

    if num_vertices == 3:
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
        cv2.putText(img, "Triangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    elif num_vertices == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w) / h

        if 0.95 <= aspect_ratio <= 1.05:
            cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)
            cv2.putText(img, "Square", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        else:
            cv2.drawContours(img, [approx], 0, (0, 255, 255), 2)
            cv2.putText(img, "Rectangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    else:
        cv2.drawContours(img, [approx], 0, (255, 0, 0), 2)
        cv2.putText(img, "Circle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
        
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
