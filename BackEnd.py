# BackEnd.py
import os
import time
from datetime import datetime

import cv2
import numpy as np
import pyautogui
from Levenshtein import ratio
from PIL import ImageGrab
from google.cloud import vision

import Logic
from Colors import TEXTBOX_COLOR, DOCUMENT_AREA_COLOR, LadyCard, \
    LadyCardSecondary, TICKETCOLOR, TICKETCOLOR2

from Positions import STAMP_TRAY_POSITION, APPROVAL_STAMP_POSITION, PASSPORT_SLOT_POSITION, DOCUMENT_DROP_POSITION, \
    REJECTED_PASSPORT_POSITION, REJECTED_STAMP_POSITION, \
    INSPECT_BUTTON_POSITION, PASSPORT_POSITION, PASSPORT_SIDE_POSITION, REGIONAL_MAP_POSITION, \
    RULE_BOOK_POSITION, RULE_BOOK_SLOT_POSITION, RULE_BOOK_BASICS_POSITION, \
    PASSPORT_RULE_POSITION, INTERROGATE_POSITION, REPLY_TEXT_BOX_POSITION, TICKET_RULE_POSITION, \
    SECONDARY_DOCUMENT_POSITION, DOCUMENT_AREA_POSITION, SECONDARY_DOCUMENT_SLOT_POSITION

Matching = "MATCHING"

# Initialize the Google Vision client
os.environ[
    'GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Divuff.DESKTOP-PBPI579/Documents/papers-please-382221-065ea6c09fa5.json'
client = vision.ImageAnnotatorClient()


def get_image_color(position):
    color_detect = ImageGrab.grab().load()
    return color_detect[position[0], position[1]]


def move_mouse(position):
    pyautogui.moveTo(position)


def click_mouse(position):
    move_mouse(position)
    pyautogui.click()


def drag_and_drop(start_position, end_position):
    move_mouse(start_position)
    pyautogui.mouseDown(button='left')
    move_mouse(end_position)
    time.sleep(0.3)
    pyautogui.mouseUp(button='left')


def process_passport(passport_status):
    if passport_status == "Approved":
        print("WELCOME!")
        click_mouse(STAMP_TRAY_POSITION)
        time.sleep(0.3)
        click_mouse(APPROVAL_STAMP_POSITION)
        drag_and_drop(PASSPORT_SLOT_POSITION, DOCUMENT_DROP_POSITION)

    if passport_status == "Rejected":
        click_mouse(STAMP_TRAY_POSITION)
        drag_and_drop(PASSPORT_SLOT_POSITION, REJECTED_PASSPORT_POSITION)
        time.sleep(0.3)
        click_mouse(REJECTED_STAMP_POSITION)
        drag_and_drop(REJECTED_PASSPORT_POSITION, DOCUMENT_DROP_POSITION)


def reset_person():
    Logic.PersonPresent = False
    Logic.PassportPresent = False
    Logic.StampingTime = False
    Logic.NoPassport = False
    Logic.NextPerson = False
    Logic.CorrectDate = False
    Logic.CorrectCity = False
    Logic.PersonGenderMatch = False
    Logic.PhotoPersonMatch = False
    Logic.TicketPresent = False
    Logic.ValidTicket = False
    Logic.DocumentStatus = False
    Logic.NoTicket = False
    Logic.TextBoxPresent = False



def return_documents(documentpos):
    drag_and_drop(documentpos, DOCUMENT_DROP_POSITION)


def inspection(first_inspect_item_location, second_inspect_item_location):
    click_mouse(INSPECT_BUTTON_POSITION)
    click_mouse(first_inspect_item_location)
    click_mouse(second_inspect_item_location)


def move_intrusive_object():
    drag_and_drop(PASSPORT_POSITION, PASSPORT_SIDE_POSITION)


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


def inspect_detect(inspect_position):
    time.sleep(2)
    text = textdetect(inspect_position)
    text = text.strip()

    print(text)
    click_mouse(INSPECT_BUTTON_POSITION)
    if Matching in text:
        text = "MATCHING"
        print(text)

    if ratio(text, Matching) >= 0.75:
        return True
    else:
        return False


def compare_dates(inspect_position, reference_date):
    # Extract date from input text
    detected_date_text = textdetect(inspect_position).strip()
    print(detected_date_text)

    # Clean up date string
    detected_date_text = detected_date_text.replace("EXP. ", "")
    detected_date_text = detected_date_text.replace(".", "-")

    # Convert date string to list
    date_list = list(detected_date_text)

    # Replace '8' with '0' at the first and fourth positions
    if date_list[0] == '8':
        date_list[0] = '0'
    if date_list[0] == '6':
        date_list[0] = '0'
    if date_list[1] == '9':
        date_list[1] = '0'

    # Convert list back to string
    detected_date_text = ''.join(date_list)
    print(detected_date_text)
    # Convert date string to a datetime object
    detected_date = datetime.strptime(detected_date_text, "%m-%d-%Y").date()
    reference_date = datetime.strptime(reference_date, "%m-%d-%Y").date()

    return detected_date, reference_date


def on_date_check(inspect_position, reference_date):
    detected_date, reference_date = compare_dates(inspect_position, reference_date)
    if detected_date == reference_date:
        return True
    else:
        return False


def up_to_date_check(inspect_position, reference_date):
    detected_date, reference_date = compare_dates(inspect_position, reference_date)
    if detected_date >= reference_date:
        return True
    else:
        return False


def text_within(input_text, input_text2):
    input_text = input_text.strip()
    input_text2 = input_text2.strip()

    if input_text in input_text2 and input_text != " ":
        return True
    else:
        return False


def compare_text(inspect_position, inspect_position2):
    text = textdetect(inspect_position)
    text2 = textdetect(inspect_position2)

    text = text.strip()
    text2 = text2.strip()

    if text == text2:
        return True
    else:
        return False


def compare_city(city_pos, issuing_city_pos):
    click_mouse(REGIONAL_MAP_POSITION)
    click_mouse(Logic.COUNTRY_POSITION)

    text = textdetect(city_pos)
    text2 = textdetect(issuing_city_pos)

    print(text)
    print(text2)
    result = text_within(text, text2)
    return result


def lack_of_document(document_type):
    texbox_area = ()

    drag_and_drop(RULE_BOOK_POSITION, RULE_BOOK_SLOT_POSITION)
    click_mouse(RULE_BOOK_BASICS_POSITION)

    if document_type == "Passport":
        inspection(PASSPORT_RULE_POSITION, PASSPORT_POSITION)

        time.sleep(1.5)
        click_mouse(INTERROGATE_POSITION)

        while texbox_area != TEXTBOX_COLOR:
            texbox_area = get_image_color(REPLY_TEXT_BOX_POSITION)
        else:
            time.sleep(1.5)
            document_status = passport_check()
            return document_status


    elif document_type == "Ticket":
        inspection(TICKET_RULE_POSITION, SECONDARY_DOCUMENT_POSITION)

        time.sleep(1.5)
        click_mouse(INTERROGATE_POSITION)

        while texbox_area != TEXTBOX_COLOR:
            texbox_area = get_image_color(REPLY_TEXT_BOX_POSITION)
        else:
            time.sleep(2)
            document_status = ticket_check()
            return document_status


def passport_check():
    area = get_image_color(DOCUMENT_AREA_POSITION)
    if area != DOCUMENT_AREA_COLOR and area != TICKETCOLOR:
        # MOVE PASSPORT TO SLOT
        drag_and_drop(PASSPORT_POSITION, PASSPORT_SLOT_POSITION)
        return True
    else:
        return False


def ticket_check():
    area = get_image_color(DOCUMENT_AREA_POSITION)
    print(area)
    if area == TICKETCOLOR or area == TICKETCOLOR2:
        drag_and_drop(SECONDARY_DOCUMENT_POSITION, SECONDARY_DOCUMENT_SLOT_POSITION)

        return True

    else:

        return False


def textbox_check(text_box_location):
    area = get_image_color(text_box_location)
    if area == TEXTBOX_COLOR:
        time.sleep(1.5)
        return True
    else:
        return False


def lady_worker():
    lady_stat = get_image_color(PASSPORT_POSITION)
    if lady_stat == LadyCard or lady_stat == LadyCardSecondary:
        drag_and_drop(PASSPORT_POSITION, PASSPORT_SIDE_POSITION)
        print("Lady Worker Card in the way!")


def set_country_positions(input_color):
    country_dict = Logic.country_dict
    if input_color in country_dict:
        country_data = country_dict[input_color]

        Logic.NAME = country_data["name"]
        Logic.PHOTO_POSITION = country_data["PHOTO_POSITION"]
        Logic.GENDER_POSITION = country_data["GENDER_POSITION"]
        Logic.COUNTRY_POSITION = country_data["COUNTRY_POSITION"]
        Logic.CITY_POSITION = country_data["CITY_POSITION"]
        Logic.DATE_POSITION = country_data["DATE_POSITION"]
        Logic.PHOTO_PERSON_INSPECT_POSITION = country_data["PHOTO_PERSON_INSPECT_POSITION"]
        Logic.PERSON_GENDER_INSPECT_POSITION = country_data["PERSON_GENDER_INSPECT_POSITION"]

        print(Logic.NAME)






