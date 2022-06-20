import cv2
import pytesseract

img = cv2.imread('Resources/dauphine1.jpeg')

# Adding custom options
#custom_config = r'--oem 3 --psm 6'
#pytesseract.image_to_string(img, config=custom_config)
text = pytesseract.image_to_string(img)
print(text)
print("End ...")