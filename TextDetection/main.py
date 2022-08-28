import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('text.jpg')
img = cv2.resize(img, None, fx=0.8, fy=0.8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)
print(text)

cv2.imshow('gray img', gray)
cv2.imshow('img', img)
cv2.waitKey(0)