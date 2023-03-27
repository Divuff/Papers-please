# cv2.cvtColor takes a numpy ndarray as an argument
import time

import numpy as nm
import pyautogui
import pytesseract
import Levenshtein

# importing OpenCV
import cv2

from PIL import ImageGrab

Matching = "MATCHING"
Text = ""

TicketDateInspectTopX = 660
TicketDateInspectBottomX = 950
TicketDateInspectTopY = 850
TicketDateInspectBottomY = 1100



# Path of tesseract executable
time.sleep(2)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = ImageGrab.grab(bbox=(TicketDateInspectTopX, TicketDateInspectTopY, TicketDateInspectBottomX, TicketDateInspectBottomY))

# Converted the image to monochrome for it to be easily
# read by the OCR and obtained the output String.
Text = pytesseract.image_to_string(
    cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
    lang='eng')


Text = Text.strip()
print(Text)

similarity_ratio = Levenshtein.ratio(Text, Matching)
if similarity_ratio >= 0.75:
    print("The strings are similar")
else:
    print("The strings are not similar")
