import cv2
print("Hello from OpenCV platform")
img1 = cv2.imread("Resources/citroen1.jpg")
cv2.imshow('Dauphine',img1)
cv2.waitKey(7000)