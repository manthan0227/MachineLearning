import cv2
import pytesseract
import folium
from opencage.geocoder import OpenCageGeocode

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = cv2.imread('images/1.png')
img = cv2.resize(img, None, fx=0.8, fy=0.8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)
location = text
# print(location)

#api key from opencagedata.com
key = "bb712581856d4e9d86c0487bc423c625"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

# print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

# Save map in html file
myMap.save("mylocation.html")

# cv2.imshow('gray', gray)
# cv2.imshow('window', img)
# cv2.waitKey(0)
