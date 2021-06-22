
import cv2
import matplotlib.pyplot as plt
import numpy


image1 = cv2.imread('dark1.jpg')
image2 = cv2.imread('mid1.jpg')
image3 = cv2.imread('light1.jpg')

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)


cv2.imshow("dark1",gray_image1)
cv2.imshow("mid2",gray_image2)
cv2.imshow("light1",gray_image3)
cv2.waitKey(0)

#calculating histogram
histogram1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
histogram2= cv2.calcHist([gray_image2], [0], None, [256], [0, 256])
histogram3 = cv2.calcHist([gray_image3], [0], None, [256], [0, 256])

plt.plot(histogram1, color='k')
plt.show()
plt.plot(histogram2, color='k')
plt.show()
plt.plot(histogram3, color='k')
plt.show()


