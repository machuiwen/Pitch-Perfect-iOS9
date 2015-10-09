from cv2 import *
import cv2

width = 60 * 3
im = imread('IMG_0609.jpeg')
im = cv2.resize(im, (width, width))
imwrite("Pitch Perfect/res/icon_%d.png"%width, im)