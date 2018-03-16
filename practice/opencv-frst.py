import cv2
import numpy as np
import matplotlib.pyplot as pyplot

def show(name, img):
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.plot([])
    plt.show()
    '''
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

img = cv2.imread('../img/img7.jpg', cv2.IMREAD_GRAYSCALE)

show('image', img)
