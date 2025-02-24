# import required packages
import numpy as np
import cv2

# load the image and display it to our screen
image = cv2.imread('image.jpg')
cv2.imshow("Original", image)
cv2.waitKey(0)

# Define a translation  matrix (M) to shift the image 40 pixels
# to the right and 50 pixels downwards.
M = np.float32([[1, 0, 40], [0, 1, 50]])

# get image's width and height.
img_width = image.shape[1]
img_height = image.shape[0]
print(f"translation matrix:\n {M} \n Image's width: {img_width} \n Image's height: {img_height}")

# Shift the image 40 pixels rightwards and 50 pixels downwards
shifted_image = cv2.warpAffine(image, M, (img_width, img_height))
cv2.imshow("Shifted Down and Right", shifted_image)
cv2.waitKey(0)

# shift the image 70 pixels leftwards and 120 pixels rightwards
# by specifying negative values for the x and y directions,
# respectively
M = np.float32([[1, 0, -70], [0, 1, -120]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)

