# ----------------------------
# Author : Benzee (bz7002@gmail.com)
# functions file
#
#-----------------------------
import cv2
import imutils
# function 1
def DisplayImage(title, image):
    cv2.imshow(title, image)
    return 0