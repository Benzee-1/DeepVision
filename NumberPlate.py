import cv2
import imutils
import pytesseract
# Load and resize to 300 width of the input image
imagein = cv2.imread('Resources/dauphine1.jpeg')
image = imutils.resize(imagein, width=300 )
cv2.imshow("original image", image)
#cv2.waitKey(0)

# Convert the input image to gray scale image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("greyed image", gray_image)
#cv2.waitKey(0)

# REduce noises in the gray scale image
gray_image = cv2.bilateralFilter(gray_image, 11, 17, 17)
cv2.imshow("smoothened image", gray_image)
#cv2.waitKey(0)

# Detect edge of the smoothened image
edged = cv2.Canny(gray_image, 30, 200)
cv2.imshow("edged image", edged)
#cv2.waitKey(0)

# Find contours of the edge image
cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1=image.copy()
cv2.drawContours(image1,cnts,-1,(0,255,0),3)
cv2.imshow("contours",image1)
#cv2.waitKey(0)

# Drawing of the identified contours
cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
screenCnt = None
image2 = image.copy()
cv2.drawContours(image2,cnts,-1,(0,255,0),3)
cv2.imshow("Top 30 contours",image2)
#cv2.waitKey(0)

#Find 4-sides contours
i=7
for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) == 4:
                screenCnt = approx

# Cropping the rectangular part identified as license plate
x,y,w,h = cv2.boundingRect(c)
new_img=image[y:y+h,x:x+w]
cv2.imwrite('./'+str(i)+'.png',new_img)
i+=1
break
print("End ...")