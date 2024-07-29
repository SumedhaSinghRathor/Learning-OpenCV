import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('chappell roan.png')
img2 = cv2.imread('renee rapp.png')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.imshow(img1)
ax1.set_title('Image 1')
ax2.imshow(img2)
ax2.set_title('Image 2')

plt.show()
