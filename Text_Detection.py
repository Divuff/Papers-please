import os
import re
import time
import Levenshtein
import cv2
import numpy as np
import pytesseract
from PIL import ImageGrab
from google.cloud import vision
from Pos import positions




# Initialize the Google Vision client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/dunke/Downloads/papers-please-382221-ee7f3abe8cd7.json'
client = vision.ImageAnnotatorClient()
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def find_two_word_coordinates(word1, word2):
    full_word = (word1 + " " + word2)
    print(full_word)

    # Convert the image to grayscale and save it as a temporary file
    image = np.array(ImageGrab.grab())
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_image_path = '../temp_image.png'
    cv2.imwrite(temp_image_path, gray_image)

    # Read the temporary image file and send it to Google Vision API
    with open(temp_image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)

    # Extract the text from the response
    annotations = response.text_annotations

    # Find the bounding box coordinates for the first word
    word1_coordinates = None
    for i in range(len(annotations)):
        text = annotations[i].description
        similarity = Levenshtein.ratio(text, word1)
        if similarity >= 0.75:
            word1_coordinates = annotations[i].bounding_poly.vertices
            break

    # Find the bounding box coordinates for the second word
    word2_coordinates = None
    for i in range(len(annotations)):
        text = annotations[i].description
        similarity = Levenshtein.ratio(text, word2)
        if similarity >= 0.75:
            word2_coordinates = annotations[i].bounding_poly.vertices
            break
        
    # Combine the bounding box coordinates if both words are found
    if word1_coordinates and word2_coordinates:
        top_left_x = min(word1_coordinates[0].x, word2_coordinates[0].x)
        top_left_y = min(word1_coordinates[0].y, word2_coordinates[0].y)
        bottom_right_x = max(word1_coordinates[2].x, word2_coordinates[2].x)
        bottom_right_y = max(word1_coordinates[2].y, word2_coordinates[2].y)
        coordinates = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)


        detected_text = ""
        while full_word != detected_text:
            detected_text = textdetect(coordinates)
            detected_text = detected_text.replace("-", " ")
            detected_text = detected_text.replace(",", "")
            detected_text = detected_text.replace(".", "")
            detected_text = re.sub(r'O', '0', detected_text)
            
            print(detected_text)

            if full_word != detected_text:
                cords = list(coordinates)
                cords[0] -= 1  # Subtract 1 from the first element
                cords[1] -= 1  # Subtract 1 from the second element
                cords[2] += 1  # Add 1 from the second element
                cords[3] += 1  # Add 1 from the second element
                coordinates = tuple(cords)
                print(coordinates)

        
        return(coordinates)

    else:
        print("One or both words not found.")


def find_word_coordinates(word):
    # Capture the screen image
    image = np.array(ImageGrab.grab())

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image as a temporary file
    temp_image_path = '../temp_image.png'
    cv2.imwrite(temp_image_path, gray_image)

    # Read the temporary image file and send it to Google Vision API
    with open(temp_image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)

    # Extract the text annotations from the response
    annotations = response.text_annotations

    # Find the bounding box coordinates for the word
    word_coordinates = None
    for i in range(len(annotations)):
        text = annotations[i].description
        similarity = Levenshtein.ratio(text, word)
        if similarity >= 0.75:
            word_coordinates = annotations[i].bounding_poly.vertices
            break

    if word_coordinates:
        top_left_x = word_coordinates[0].x
        top_left_y = word_coordinates[0].y
        bottom_right_x = word_coordinates[2].x
        bottom_right_y = word_coordinates[2].y
        coordinates = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

        detected_text = ""
        while word != detected_text:
            detected_text = textdetect(coordinates)
            detected_text = detected_text.replace("-", " ")
            detected_text = detected_text.replace(",", "")
            detected_text = detected_text.replace(".", "")
            
            print(detected_text)
            print(coordinates)

            if word != detected_text:
                cords = list(coordinates)
                cords[0] -= 1  # Subtract 1 from the first element
                cords[1] -= 1  # Subtract 1 from the second element
                cords[2] += 1  # Add 1 from the second element
                cords[3] += 1  # Add 1 from the second element
                coordinates = tuple(cords)
                print(coordinates)

        
        
        return coordinates

    else:
        print(f"Word '{word}' not found.")


def find_date_coordinates(word):
    # Capture the screen image
    image = np.array(ImageGrab.grab())

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image as a temporary file
    temp_image_path = '../temp_image.png'
    cv2.imwrite(temp_image_path, gray_image)

    # Read the temporary image file and send it to Google Vision API
    with open(temp_image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)

    # Extract the text annotations from the response
    annotations = response.text_annotations

    # Find the bounding box coordinates for the word
    word_coordinates = None
    for i in range(len(annotations)):
        text = annotations[i].description
        similarity = Levenshtein.ratio(text, word)
        if similarity >= 0.75:
            word_coordinates = annotations[i].bounding_poly.vertices
            break

    if word_coordinates:
        top_left_x = word_coordinates[0].x
        top_left_y = word_coordinates[0].y
        bottom_right_x = word_coordinates[2].x
        bottom_right_y = word_coordinates[2].y
        coordinates = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

        detected_text = ""
        while word != detected_text:
            detected_text = textdetect(coordinates)
        
            print(detected_text)
            print(coordinates)

            if word != detected_text:
                cords = list(coordinates)
                cords[0] -= 1  # Subtract 1 from the first element
                cords[1] -= 1  # Subtract 1 from the second element
                cords[2] += 1  # Add 1 from the second element
                cords[3] += 1  # Add 1 from the second element
                coordinates = tuple(cords)
                print(coordinates)

        
        return coordinates

    else:
        print(f"Word '{word}' not found.")


def word_search(word, textpos):
    # Capture the screen image
    image = np.array(ImageGrab.grab())

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image as a temporary file
    temp_image_path = '../temp_image.png'
    cv2.imwrite(temp_image_path, gray_image)

    # Read the temporary image file and send it to Google Vision API
    with open(temp_image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)

    # Extract the text annotations from the response
    annotations = response.text_annotations

    # Find the bounding box coordinates for the word
    word_coordinates = textpos
    
    if word_coordinates:
        top_left_x = word_coordinates[0].x
        top_left_y = word_coordinates[0].y
        bottom_right_x = word_coordinates[2].x
        bottom_right_y = word_coordinates[2].y
        coordinates = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

        detected_text = ""
        while word != detected_text:
            detected_text = textdetect(coordinates)
            detected_text = detected_text.replace("-", " ")
            detected_text = detected_text.replace(",", "")
            detected_text = detected_text.replace(".", "")
            
            print(detected_text)
            print(coordinates)

            if word != detected_text:
                cords = list(coordinates)
                cords[0] -= 1  # Subtract 1 from the first element
                cords[1] -= 1  # Subtract 1 from the second element
                cords[2] += 1  # Add 1 from the second element
                cords[3] += 1  # Add 1 from the second element
                coordinates = tuple(cords)
                print(coordinates)

        
        
        return coordinates

    else:
        print(f"Word '{word}' not found.")

def textdetect(inspect_position):
    # Convert the image to grayscale and save it as a temporary file
    image = np.array(ImageGrab.grab(bbox=inspect_position))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp_image_path = '../temp_image.png'
    cv2.imwrite(temp_image_path, gray_image)

    # Read the temporary image file and send it to Google Vision API
    with open(temp_image_path, 'rb') as image_file:
        content = image_file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)

    # Extract the text from the response
    text = response.text_annotations[0].description if response.text_annotations else ''

    return text

def find_word_coordinates_tes(word):
    # Capture the screen image
    image = np.array(ImageGrab.grab())

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract the text annotations from the response
    annotations = pytesseract.image_to_string(gray_image, lang='eng')
    annotations = annotations.replace("-", " ")
    annotations = annotations.replace(",", "")
    annotations = annotations.replace(".", "")
    # Print out the annotations for debugging
    print("Annotations:")
    print(annotations)

    # Find the bounding box coordinates for the word
    word_coordinates = None
    for i, text in enumerate(annotations.split('\n')):
        similarity = Levenshtein.ratio(text, word)
        print(f"Text: {text}, Similarity: {similarity}")  # Print similarity score for debugging
        if similarity >= 0.75:
            word_coordinates = annotations[i]  # Adjusted here if needed
            break

    # Print the found word coordinates for debugging
    print("Word coordinates:", word_coordinates)


    if word_coordinates:
        top_left_x = word_coordinates[0].x
        top_left_y = word_coordinates[0].y
        bottom_right_x = word_coordinates[2].x
        bottom_right_y = word_coordinates[2].y
        coordinates = (top_left_x, top_left_y, bottom_right_x, bottom_right_y)

        detected_text = ""
        while word != detected_text:
            detected_text = textdetect(coordinates)
            
            
            print(detected_text)
            print(coordinates)

            if word != detected_text:
                cords = list(coordinates)
                cords[0] -= 1  # Subtract 1 from the first element
                cords[1] -= 1  # Subtract 1 from the second element
                cords[2] += 1  # Add 1 from the second element
                cords[3] += 1  # Add 1 from the second element
                coordinates = tuple(cords)
                print(coordinates)

        
        
        return coordinates

    else:
        print(f"Word '{word}' not found.")


def tes_detection(inspect_position):
    image = np.array(ImageGrab.grab(bbox=inspect_position))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    text = pytesseract.image_to_string(
        gray_image, lang='eng')

    text = text.strip()
    print(text)


find_word_coordinates_tes("NIVEKA")
