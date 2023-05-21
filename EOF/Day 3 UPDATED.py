import time

import cv2
import pyautogui
from PIL import ImageGrab
import os
import numpy as np
from google.cloud import vision
from Levenshtein import ratio
from datetime import datetime

from Colors import ARSTOTZKA_COLOR, PERSON_COLOR, TEXTBOX_COLOR, DAY_COLOR, DOCUMENT_AREA_COLOR, WALL_COLOR, \
    ANTEGRIA_COLOR, OBRISTAN_COLOR, UNITEDFED_COLOR, REPUBLIA_COLOR, IMPOR_COLOR, KOLECHIA_COLOR, LadyCard, \
    LadyCardSecondary, TICKETCOLOR, TICKETCOLOR2

# Logic Variables
PersonPresent = False
PassportPresent = False
StampingTime = False
NoPassport = False
CorrectDate = False
CorrectCity = False
PhotoPersonMatch = False
PersonGenderMatch = False
NextPerson = False
TextBoxPresent = False
TicketPresent = False
ValidTicket = False
DocumentStatus = False
NoTicket = False

Arstotzkan = False

DATE_POSITION = ()
PHOTO_POSITION = ()
CITY_POSITION = ()
GENDER_POSITION = ()

COUNTRY_POSITION = ()
PHOTO_GENDER_INSPECT_POSITION = ()
PERSON_GENDER_INSPECT_POSITION = ()
PHOTO_PERSON_INSPECT_POSITION = ()

PRIMARY_TEXT_BOX_POSITION = (140, 535)
PASSPORT_SIDE_POSITION = (175, 1085)
CLOCK_POSITION = (200, 1320)

PASSPORT_POSITION = (475, 1085)
DOCUMENT_DROP_POSITION = (480, 700)
PERSON_POSITION = (490, 850)
SECONDARY_DOCUMENT_POSITION = (500, 1065)
INTERROGATE_POSITION = (500, 1230)
DOCUMENT_AREA_POSITION = (500, 1080)

RULE_BOOK_POSITION = (640, 1250)
REJECTED_PERSON_LEAVING_POSITION = (700, 430)
SPEAKER_POSITION = (830, 370)
REPLY_TEXT_BOX_POSITION = (840, 600)
LEVER_POSITION = (850, 550)
BOOKMARK_POSITION = (870, 750)
ACCEPTED_PERSON_LEAVING_POSITION = (960, 430)

PASSPORT_RULE_POSITION = (1000, 850)
TICKET_RULE_POSITION = (1035, 1055)
SECONDARY_DOCUMENT_SLOT_POSITION = (1260, 625)

RULE_BOOK_SLOT_POSITION = (1300, 1050)
ISSUING_CITIES_POSITION = (1400, 1120)
DAY_TEST_POSITION = (1444, 180)
RULE_BOOK_BASICS_POSITION = (1500, 910)

REGIONAL_MAP_POSITION = (1510, 970)
REJECTED_STAMP_POSITION = (1600, 695)
REJECTED_PASSPORT_POSITION = (1600, 950)

PASSPORT_BORDER_POSITION = (1845, 950)

PASSPORT_SLOT_POSITION = (2100, 950)
APPROVAL_STAMP_POSITION = (2100, 730)
APPROVED_PASSPORT_POSITION = (2100, 950)

INSPECT_BUTTON_POSITION = (2350, 1320)
STAMP_TRAY_POSITION = (2400, 730)

ISSUING_CITY_POS = (1370, 1080, 1620, 1200)

TICKET_DATE_POSITION = (1330, 645, 1505, 690)

IDCARD_DISTRICT_POSITION = (1020, 525, 1305, 550)
IDCARD_NAME_POSITION = (1200, 562, 1362, 617)
IDCARD_PHOTO_POSITION = (1100, 675)

IDCARD_PASSPORT_PHOTO_POSITION = (1408, 846, 1615, 917)

DISTRICT_POSITION = (910, 900, 1140, 1200)

ENTRY_PERMIT_NAME_POSITION = (1214, 598)
ENTRY_PERMIT_ID_POSITION = (1215, 731)
ENTRY_PERMIT_PURPOSE_POSITION = (1320, 794)
ENTRY_PERMIT_DURATION_POSITION = (1315, 860)
ENTRY_PERMIT_DATE_POSITION = (1315, 918)

Matching = "MATCHING"
Date = "11-25-1982"

# Initialize the Google Vision client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Divuff.DESKTOP-PBPI579/Documents/papers-please-382221-065ea6c09fa5.json'
client = vision.ImageAnnotatorClient()


# Functions
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


def approve_passport():
    print("WELCOME!")
    click_mouse(STAMP_TRAY_POSITION)
    time.sleep(0.3)
    click_mouse(APPROVAL_STAMP_POSITION)
    drag_and_drop(PASSPORT_SLOT_POSITION, DOCUMENT_DROP_POSITION)


def reject_passport():
    click_mouse(STAMP_TRAY_POSITION)
    drag_and_drop(PASSPORT_SLOT_POSITION, REJECTED_PASSPORT_POSITION)
    time.sleep(0.3)
    click_mouse(REJECTED_STAMP_POSITION)
    drag_and_drop(REJECTED_PASSPORT_POSITION, DOCUMENT_DROP_POSITION)


def reset_person():

    global PersonPresent, PassportPresent, StampingTime, NoPassport, NextPerson, CorrectCity, CorrectDate, PersonGenderMatch, \
        PhotoPersonMatch, TicketPresent, ValidTicket, DocumentStatus, NoTicket, TextBoxPresent, Arstotzkan, Foreigner
    PersonPresent = False
    PassportPresent = False
    StampingTime = False
    NoPassport = False
    NextPerson = False
    CorrectDate = False
    CorrectCity = False
    PersonGenderMatch = False
    PhotoPersonMatch = False
    TicketPresent = False
    ValidTicket = False
    DocumentStatus = False
    NoTicket = False
    TextBoxPresent = False
    Arstotzkan = False
    Foreigner = False




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
    if len(date_list) > 2 and date_list[3] == '8':
        date_list[3] = '0'

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
    click_mouse(COUNTRY_POSITION)

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
    if PersonPresent and area == TEXTBOX_COLOR:
        time.sleep(1.5)
        return True
    else:
        return False


def lady_worker():
    lady_stat = get_image_color(PASSPORT_POSITION)
    if lady_stat == LadyCard or lady_stat == LadyCardSecondary:
        drag_and_drop(PASSPORT_POSITION, PASSPORT_SIDE_POSITION)
        print("Lady Worker Card in the way!")


# DaySTART
click_mouse(LEVER_POSITION)
click_mouse(SPEAKER_POSITION)

name = ()
matching_country = ()
person_leaving_area = ()

while get_image_color(DAY_TEST_POSITION) == DAY_COLOR:

    lady_worker()

    # Person Leaving Booth Check
    if person_leaving_area == PERSON_COLOR:
        NextPerson = True
        person_leaving_area = ()
        click_mouse(SPEAKER_POSITION)
        print("Ready for Next Person")
    else:
        NextPerson = False

    # Check if person is present
    person_area = get_image_color(PERSON_POSITION)
    if person_area != WALL_COLOR:
        if not PersonPresent:
            PersonPresent = True
            print("Person Detected")
    else:
        PersonPresent = False

    # Check if text box is present
    TextBoxPresent = textbox_check(PRIMARY_TEXT_BOX_POSITION)
    if TextBoxPresent:

        PassportPresent = passport_check()
        country = get_image_color(PASSPORT_BORDER_POSITION)

        if country != ARSTOTZKA_COLOR:
            Arstotzkan = False
            Foreigner = True
            TicketPresent = ticket_check()
        else:
            Foreigner = False
            Arstotzkan = True
            print("Arstotzkan Detected")

        if PassportPresent:
            print("Passport Detected")
        else:
            NoPassport = True
            print("No Passport!")

        if TicketPresent or Arstotzkan:
            print("Ticket Present")
            NoTicket = False
        else:
            print("No ticket")
            NoTicket = True

    if NoPassport:
        DocumentStatus = lack_of_document("Passport")
        click_mouse(BOOKMARK_POSITION)

        if DocumentStatus:
            NoPassport = False
            PassportPresent = True
            StampingTime = False
        else:
            PassportPresent = False
            StampingTime = True

    elif NoTicket:
        DocumentStatus = lack_of_document("Ticket")
        click_mouse(BOOKMARK_POSITION)

        if DocumentStatus:
            NoTicket = False
            TicketPresent = True
            StampingTime = False

        else:
            TicketPresent = False
            StampingTime = True

    country = get_image_color(PASSPORT_BORDER_POSITION)

    if PersonPresent and PassportPresent:
        # Define a dictionary to store the values for each country
        country_dict = {
            ARSTOTZKA_COLOR: {
                "name": "Arstotzka",
                "PHOTO_POSITION": (1920, 1120),
                "GENDER_POSITION": (2128, 1060),
                "COUNTRY_POSITION": (1650, 1080),

                "DATE_POSITION": (2035, 1111, 2288, 1140),
                "CITY_POSITION": (2108, 1078, 2321, 1106),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 780, 2020, 870),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 865, 1490, 955),
                "PHOTO_PERSON_INSPECT_POSITION": (1145, 880, 1360, 970)
            },
            ANTEGRIA_COLOR: {
                "name": "Antegria",
                "PHOTO_POSITION": (2255, 1083),
                "GENDER_POSITION": (1947, 1073),
                "COUNTRY_POSITION": (1033, 952),

                "DATE_POSITION": (1935, 1137, 2115, 1162),
                "CITY_POSITION": (1935, 1097, 2170, 1127),
                "PHOTO_GENDER_INSPECT_POSITION": (1870, 745, 2085, 825),
                "PERSON_GENDER_INSPECT_POSITION": (1180, 870, 1400, 955),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 865, 1520, 985)
            },
            OBRISTAN_COLOR: {
                "name": "Obristan",
                "PHOTO_POSITION": (2250, 1150),
                "GENDER_POSITION": (1958, 1111),
                "COUNTRY_POSITION": (1150, 780),

                "DATE_POSITION": (1945, 1163, 2125, 1190),
                "CITY_POSITION": (1945, 1130, 2130, 1165),
                "PHOTO_GENDER_INSPECT_POSITION": (1870, 825, 2100, 900),
                "PERSON_GENDER_INSPECT_POSITION": (1185, 890, 1400, 970),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 900, 1510, 1002)
            },
            IMPOR_COLOR: {
                "name": "Impor",
                "PHOTO_POSITION": (1920, 1150),
                "GENDER_POSITION": (2128, 1054),
                "COUNTRY_POSITION": (1190, 1270),

                "DATE_POSITION": (2115, 1108, 2325, 1136),
                "CITY_POSITION": (2115, 1075, 2325, 1105),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 780, 2030, 870),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 860, 1495, 950),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 880, 1370, 970)
            },
            KOLECHIA_COLOR: {
                "name": "Kolechia",
                "PHOTO_POSITION": (1920, 1150),
                "GENDER_POSITION": (2128, 1095),
                "COUNTRY_POSITION": (1450, 810),

                "DATE_POSITION": (2115, 1145, 2300, 1178),
                "CITY_POSITION": (2115, 1115, 2330, 1143),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 815, 2020, 910),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 875, 1495, 969),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 910, 1370, 992)
            },
            UNITEDFED_COLOR: {
                "name": "UnitedFed",
                "PHOTO_POSITION": (1920, 1150),
                "GENDER_POSITION": (2128, 1095),
                "COUNTRY_POSITION": (900, 1220),

                "DATE_POSITION": (2115, 1144, 2300, 1170),
                "CITY_POSITION": (2115, 1111, 2315, 1143),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 825, 2020, 900),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 875, 1495, 969),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 900, 1400, 1000)
            },
            REPUBLIA_COLOR: {
                "name": "Republia",
                "PHOTO_POSITION": (2250, 1110),
                "GENDER_POSITION": (1962, 1055),
                "COUNTRY_POSITION": (1100, 1120),

                "DATE_POSITION": (1945, 1110, 2125, 1140),
                "CITY_POSITION": (1945, 1080, 2155, 1105),
                "PHOTO_GENDER_INSPECT_POSITION": (1875, 770, 2100, 850),
                "PERSON_GENDER_INSPECT_POSITION": (1185, 860, 1410, 950),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 880, 1520, 970)
            }
        }

        # Find the matching country in the dictionary
        for color in country_dict:
            if country == color:
                matching_country = country_dict[color]["name"]
                break

        # Assign the variables based on the matching country
        for color in country_dict:
            if country_dict[color]["name"] == matching_country:
                name = country_dict[color]["name"]
                DATE_POSITION = country_dict[color]["DATE_POSITION"]
                PHOTO_POSITION = country_dict[color]["PHOTO_POSITION"]
                CITY_POSITION = country_dict[color]["CITY_POSITION"]
                GENDER_POSITION = country_dict[color]["GENDER_POSITION"]
                COUNTRY_POSITION = country_dict[color]["COUNTRY_POSITION"]
                PERSON_GENDER_INSPECT_POSITION = country_dict[color]["PERSON_GENDER_INSPECT_POSITION"]
                PHOTO_PERSON_INSPECT_POSITION = country_dict[color]["PHOTO_PERSON_INSPECT_POSITION"]
                StampingTime = True

                break

        # Print the values of the variables for the matching country
        print(f"{name}!")

    if StampingTime:

        if TicketPresent:
            ValidTicket = on_date_check(TICKET_DATE_POSITION, Date)

        if ValidTicket or Arstotzkan:
            # MOVE RULE
            drag_and_drop(RULE_BOOK_POSITION, RULE_BOOK_SLOT_POSITION)

            # CHECK CITY
            click_mouse(REGIONAL_MAP_POSITION)
            click_mouse(COUNTRY_POSITION)

            print("Valid Ticket")
            CorrectCity = compare_city(CITY_POSITION, ISSUING_CITY_POS)
            click_mouse(BOOKMARK_POSITION)
            drag_and_drop(RULE_BOOK_SLOT_POSITION, RULE_BOOK_POSITION)


        # Validate Issuing City
        if CorrectCity:
                print("Valid issuing city!")
                CorrectDate = up_to_date_check(DATE_POSITION, Date)
        else:
            print("Invalid issuing city!")

        if CorrectDate:
                inspection(GENDER_POSITION, PERSON_POSITION)
                PersonGenderMatch = inspect_detect(PERSON_GENDER_INSPECT_POSITION)
                print("Valid Date!")
        else:
            print("Passport Out Of Date!")

        if PersonGenderMatch:
                inspection(PHOTO_POSITION, PERSON_POSITION)
                PhotoPersonMatch = inspect_detect(PHOTO_PERSON_INSPECT_POSITION)
                print("Valid Gender!")
        else:
            print("InValid Gender!")

        if PhotoPersonMatch:
                print("VALID PASSPORT!")
                approve_passport()
                reset_person()

                return_documents(SECONDARY_DOCUMENT_SLOT_POSITION)

                while person_leaving_area != PERSON_COLOR:
                    person_leaving_area = get_image_color(ACCEPTED_PERSON_LEAVING_POSITION)

        elif NoPassport and NoTicket:
                print("NO DOCUMENTS")
                reset_person()

                while person_leaving_area != PERSON_COLOR:
                    person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)

        elif NoPassport:
            print("NO PASSPORT")

            reset_person()
            return_documents(SECONDARY_DOCUMENT_SLOT_POSITION)

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)

        elif NoTicket:
                print("NO TICKET")

                reject_passport()
                reset_person()

                while person_leaving_area != PERSON_COLOR:
                    person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)

        elif not ValidTicket:
                print("INVALID TICKET")
                reject_passport()
                return_documents(SECONDARY_DOCUMENT_SLOT_POSITION)
                reset_person()


                while person_leaving_area != PERSON_COLOR:
                    person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)

        else:
                print("INVALID PASSPORT")
                reject_passport()
                return_documents(SECONDARY_DOCUMENT_SLOT_POSITION)
                reset_person()


                while person_leaving_area != PERSON_COLOR:
                    person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)
