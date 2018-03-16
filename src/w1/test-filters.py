import cv2
import numpy as np

filename = '../img/img15.jpg'

img = cv2.imread(filename)

img = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
 
filter = cv2.Canny(img,100,200)
 
cv2.imshow('Original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('Laplacian Filter',filter)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# Make a consistent size
#get largest dimension
max_dimension = max(image.shape)
#The maximum window size is 700 by 660 pixels. make it fit in that
scale = 700/max_dimension
#resize it. same width and hieght none since output is 'image'.
image = cv2.resize(image, None, fx=scale, fy=scale)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''