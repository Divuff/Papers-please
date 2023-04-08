import os
import time
import cv2
import numpy as np
from PIL import ImageGrab
from google.cloud import vision
from Levenshtein import ratio

Matching = "MATCHING"
Text = ""

CITY_INSPECT_POSITION = (1720, 1065, 1930, 1155)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Divuff/Downloads/papers-please-382221-4f331df77b8e.json'


def textdetect(inspect_position):
    # Initialize the Google Vision client
    client = vision.ImageAnnotatorClient()
    time.sleep(2)

    # Convert the image to grayscale and save it as a temporary file
    image = np.array(ImageGrab.grab(bbox=inspect_position))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_image_path = 'temp_image.png'
    cv2.imwrite(temp_image_path, gray_image)

    # Read the temporary image file and send it to Google Vision API
    with open(temp_image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)

    # Extract the text from the response
    text = response.text_annotations[0].description if response.text_annotations else ''
    text = text.strip()
    print(text)

    if ratio(text, Matching) >= 0.75:
        return True
    else:
        return False

    # Delete the temporary PNG file
    os.remove(temp_image_path)

# Validate Issuing City
CorrectCity = textdetect(CITY_INSPECT_POSITION)
if CorrectCity:
    print("Valid issuing city!")
else:
    print("Invalid issuing city!")
