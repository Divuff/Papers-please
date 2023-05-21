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
    LadyCardSecondary, TICKET_COLOR, TICKET_COLOR2

from Pos import STAMP_TRAY_POS, APPROVAL_STAMP_POS, PASSPORT_SLOT_POS, DOCUMENT_DROP_POS, \
    REJECTED_PASSPORT_POS, REJECTED_STAMP_POS, \
    INSPECT_BUTTON_POS, PASSPORT_POS, PASSPORT_SIDE_POS, REGIONAL_MAP_POS, \
    RULE_BOOK_POS, RULE_BOOK_SLOT_POS, RULE_BOOK_BASICS_POS, \
    PASSPORT_RULE_POS, INTERROGATE_POS, REPLY_TEXT_BOX_POS, TICKET_RULE_POS, \
    SECONDARY_DOCUMENT_POS, DOCUMENT_AREA_POS, SECONDARY_DOCUMENT_SLOT_POS

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
        click_mouse(STAMP_TRAY_POS)
        time.sleep(0.3)
        click_mouse(APPROVAL_STAMP_POS)
        drag_and_drop(PASSPORT_SLOT_POS, DOCUMENT_DROP_POS)

    if passport_status == "Rejected":
        click_mouse(STAMP_TRAY_POS)
        drag_and_drop(PASSPORT_SLOT_POS, REJECTED_PASSPORT_POS)
        time.sleep(0.3)
        click_mouse(REJECTED_STAMP_POS)
        drag_and_drop(REJECTED_PASSPORT_POS, DOCUMENT_DROP_POS)


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
    drag_and_drop(documentpos, DOCUMENT_DROP_POS)


def inspection(first_inspect_item_location, second_inspect_item_location):
    click_mouse(INSPECT_BUTTON_POS)
    click_mouse(first_inspect_item_location)
    click_mouse(second_inspect_item_location)


def move_intrusive_object():
    drag_and_drop(PASSPORT_POS, PASSPORT_SIDE_POS)


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
    click_mouse(INSPECT_BUTTON_POS)
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
    click_mouse(REGIONAL_MAP_POS)
    click_mouse(Logic.COUNTRY_POS)

    text = textdetect(city_pos)
    text2 = textdetect(issuing_city_pos)

    print(text)
    print(text2)
    result = text_within(text, text2)
    return result


def lack_of_document(document_type):
    texbox_area = ()

    drag_and_drop(RULE_BOOK_POS, RULE_BOOK_SLOT_POS)
    click_mouse(RULE_BOOK_BASICS_POS)

    if document_type == "Passport":
        inspection(PASSPORT_RULE_POS, PASSPORT_POS)

        time.sleep(1.5)
        click_mouse(INTERROGATE_POS)

        while texbox_area != TEXTBOX_COLOR:
            texbox_area = get_image_color(REPLY_TEXT_BOX_POS)
        else:
            time.sleep(1.5)
            document_status = passport_check()
            return document_status


    elif document_type == "Ticket":
        inspection(TICKET_RULE_POS, SECONDARY_DOCUMENT_POS)

        time.sleep(1.5)
        click_mouse(INTERROGATE_POS)

        while texbox_area != TEXTBOX_COLOR:
            texbox_area = get_image_color(REPLY_TEXT_BOX_POS)
        else:
            time.sleep(2)
            document_status = ticket_check()
            return document_status


def passport_check():
    area = get_image_color(DOCUMENT_AREA_POS)
    if area != DOCUMENT_AREA_COLOR and area != TICKET_COLOR:
        # MOVE PASSPORT TO SLOT
        drag_and_drop(PASSPORT_POS, PASSPORT_SLOT_POS)
        return True
    else:
        return False


def ticket_check():
    area = get_image_color(DOCUMENT_AREA_POS)
    print(area)
    if area == TICKET_COLOR or area == TICKET_COLOR2:
        drag_and_drop(SECONDARY_DOCUMENT_POS, SECONDARY_DOCUMENT_SLOT_POS)

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
    lady_stat = get_image_color(PASSPORT_POS)
    if lady_stat == LadyCard or lady_stat == LadyCardSecondary:
        drag_and_drop(PASSPORT_POS, PASSPORT_SIDE_POS)
        print("Lady Worker Card in the way!")


def set_country_positions(input_color):
    country_dict = Logic.country_dict
    if input_color in country_dict:
        country_data = country_dict[input_color]

        Logic.NAME = country_data["name"]
        Logic.PHOTO_POS = country_data["PHOTO_POS"]
        Logic.GENDER_POS = country_data["GENDER_POS"]
        Logic.COUNTRY_POS = country_data["COUNTRY_POS"]
        Logic.CITY_POS = country_data["CITY_POS"]
        Logic.DATE_POS = country_data["DATE_POS"]
        Logic.PHOTO_PERSON_INSPECT_POS = country_data["PHOTO_PERSON_INSPECT_POS"]
        Logic.PERSON_GENDER_INSPECT_POS = country_data["PERSON_GENDER_INSPECT_POS"]

        print(Logic.NAME)







