import cv2 as c
import numpy
import matplotlib

img_gray = c.imread('D:\Programming\Python\Github\Python_General\OpenCV\\moar i want moar.jpg', c.IMREAD_GRAYSCALE)
img_color = c.imread('D:\Programming\Python\Github\Python_General\OpenCV\\moar i want moar.jpg', c.IMREAD_COLOR)

img_mixed = c.addWeighted(img_color, .5, img_color, -.4, 0)

c.imshow('Wallpaper', img_mixed)

c.imwrite('D:\Programming\Python\Github\Python_General\OpenCV\\i got moar (gray).jpg', img_gray)
c.imwrite('D:\Programming\Python\Github\Python_General\OpenCV\\i got moar (color).jpg', img_color)

c.waitKey(0)		# miliseconds
