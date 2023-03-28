import time

import cv2
import pyautogui
from PIL import ImageGrab
import pytesseract
import numpy as nm
import Levenshtein


from Colors import ARSTOTZKA_COLOR, PERSON_COLOR, TEXTBOX_COLOR, DAY_COLOR, DOCUMENT_AREA_COLOR, DESK_COLOR, WALL_COLOR, \
    ANTEGRIA_COLOR, OBRISTAN_COLOR, UNITEDFED_COLOR, REPUBLIA_COLOR, IMPOR_COLOR, KOLECHIA_COLOR, LadyCard, LadyCardSecondary

# Logic Variables
PersonPresent = False
PassportPresent = False
StampingTime = False
PassportStatus = False
CorrectDate = False
CorrectCity = False
PhotoPersonMatch = False
PersonGenderMatch = False
PhotoGenderMatch = False
NextPerson = False
TextBoxPresent = False
VisPassportPresent = False

DATE_POSITION = ()
PHOTO_POSITION = ()
CITY_POSITION = ()
GENDER_POSITION = ()

COUNTRY_POSITION = ()
DATE_INSPECT_POSITION = ()
CITY_INSPECT_POSITION = ()
PHOTO_GENDER_INSPECT_POSITION = ()
PERSON_GENDER_INSPECT_POSITION = ()
PHOTO_PERSON_INSPECT_POSITION = ()

SPEAKER_POSITION = (830, 370)
LEVER_POSITION = (850, 550)
RULE_BOOK_SLOT_POSITION = (1300, 1050)
RULE_BOOK_POSITION = (640, 1250)
PASSPORT_POSITION = (475, 1085)
PASSPORT_SLOT_POSITION = (2100, 950)
REGIONAL_MAP_POSITION = (1510, 970)
INSPECT_BUTTON_POSITION = (2350, 1320)
ISSUING_CITIES_POSITION = (1400, 1120)
PERSON_POSITION = (490, 850)
DOCUMENT_DROP_POSITION = (480, 600)
DAY_TEST_POSITION = (1444, 180)
BOOKMARK_POSITION = (870, 750)
CLOCK_POSITION = (200, 1320)
ACCEPTED_PERSON_LEAVING_POSITION = (960, 450)
REJECTED_PERSON_LEAVING_POSITION = (700, 450)
RULE_BOOK_BASICS_POSITION = (1500, 910)
PASSPORT_RULE_POSITION = (1000, 850)
INTERROGATE_POSITION = (500, 1230)
PASSPORT_BORDER_POSITION = (1845, 950)
TEXT_BOX_POSITION = (140, 535)
DOCUMENT_AREA_POSITION = (500, 1080)
PASSPORT_SIDE_POSITION = (175, 1085)
STAMP_TRAY_POSITION = (2400, 730)
APPROVAL_STAMP_POSITION = (2100, 730)
REJECTED_STAMP_POSITION = (1600, 695)
APPROVED_PASSPORT_POSITION = (2100, 950)
REJECTED_PASSPORT_POSITION = (1600, 950)

Matching = "MATCHING"
Date = ""
City = ""


# Functions
def get_image_color(position):
    color_detect = ImageGrab.grab().load()
    return color_detect[position[0], position[1]]


def move_mouse(position):
    pyautogui.moveTo(position)
    time.sleep(0.3)


def click_mouse(position):
    move_mouse(position)
    pyautogui.click()


def drag_and_drop(start_position, end_position):
    move_mouse(start_position)
    pyautogui.mouseDown(button='left')
    move_mouse(end_position)
    pyautogui.mouseUp(button='left')


def approve_passport():
    print("WELCOME!")
    click_mouse(STAMP_TRAY_POSITION)
    click_mouse(APPROVAL_STAMP_POSITION)
    drag_and_drop(PASSPORT_SLOT_POSITION, DOCUMENT_DROP_POSITION)


def reject_passport():
    print("FOREIGN SCUM")
    click_mouse(STAMP_TRAY_POSITION)
    drag_and_drop(PASSPORT_SLOT_POSITION, REJECTED_PASSPORT_POSITION)
    click_mouse(REJECTED_STAMP_POSITION)
    drag_and_drop(REJECTED_PASSPORT_POSITION, DOCUMENT_DROP_POSITION)


def reset_person():
    global PersonPresent, PassportPresent, Arstotzkan, StampingTime, NoPassport, NextPerson
    PersonPresent = False
    PassportPresent = False
    Arstotzkan = False
    StampingTime = False
    NoPassport = False
    NextPerson = False


def move_intrusive_object():
    drag_and_drop(PASSPORT_POSITION, PASSPORT_SIDE_POSITION)


def textdetect(inspect_position, object_variable, object_boolean):
    # Path of tesseract executable
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    object_variable = ImageGrab.grab(bbox=inspect_position)

    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    object_variable = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(object_variable), cv2.COLOR_BGR2GRAY),
        lang='eng')

    object_variable = object_variable.strip()
    if Levenshtein.ratio(object_variable, Matching) >= 0.75:
        print(object_variable, "Match!")
        object_boolean = True
    else:
        object_boolean = False
        print("Incorrect City!")


# DaySTART
click_mouse(LEVER_POSITION)
click_mouse(SPEAKER_POSITION)
time.sleep(1)

while get_image_color(DAY_TEST_POSITION) == DAY_COLOR:
    # Check if Person has left the booth
    if person_leaving_area != PERSON_COLOR:
        NextPerson = False
    else:
        NextPerson = True
        person_leaving_area = ()
        click_mouse(SPEAKER_POSITION)
        print("Ready for Next Person")

    # Check if person is present
    if person_area != WALL_COLOR:
        if not PersonPresent:
            PersonPresent = True
            print("Person Detected")
    else:
        PersonPresent = False
        person_area = get_image_color(PERSON_POSITION)

    #lady_card_area = get_image_color(PASSPORT_POSITION)
    #if LadyWorker == LadyCard or LadyWorker == LadyCardSecondary:
        #move_intrusive_object()
        #print("Lady Worker Card in the way!")

        # Check if text box is present
        textbox_area = get_image_color(TEXT_BOX_POSITION)
        if PersonPresent and textbox_area == TEXTBOX_COLOR:
            time.sleep(1.5)

            # Check if passport is present in Document area
            document_area = get_image_color(DOCUMENT_AREA_POSITION)

            if document_area != DOCUMENT_AREA_COLOR:
                # MOVE PASSPORT TO SLOT
                drag_and_drop(PASSPORT_POSITION, PASSPORT_SLOT_POSITION)
                PassportPresent = True
                print("Passport Detected")
            else:
                NoPassport = True
                PassportPresent = False
                print("No Passport!")

        # Check passport border color to determine country
        country = get_image_color(PASSPORT_BORDER_POSITION)

    if PersonPresent and PassportPresent:
        # Define a dictionary to store the values for each country
        country_dict = {
            ARSTOTZKA_COLOR: {
                "name": "Arstotzka",
                "DATE_POSITION": (2175, 1120),
                "PHOTO_POSITION": (1920, 1120),
                "CITY_POSITION": (2150, 1090),
                "GENDER_POSITION": (2128, 1060),
                "COUNTRY_POSITION": (1650, 1080),

                "DATE_INSPECT_POSITION": (1070, 1165, 1295, 1255),
                "CITY_INSPECT_POSITION": (1740, 1070, 1965, 1160),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 780, 2020, 870),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 865, 1490, 955),
                "PHOTO_PERSON_INSPECT_POSITION": (1145, 880, 1360, 970)
            },
            ANTEGRIA_COLOR: {
                "name": "Antegria",
                "DATE_POSITION": (2020, 1145),
                "PHOTO_POSITION": (2255, 1083),
                "CITY_POSITION": (1987, 1112),
                "GENDER_POSITION": (1947, 1073),
                "COUNTRY_POSITION": (1033, 952),

                "DATE_INSPECT_POSITION": (960, 1170, 1240, 1290),
                "CITY_INSPECT_POSITION": (1660, 1080, 1870, 1170),
                "PHOTO_GENDER_INSPECT_POSITION": (1870, 745, 2085, 825),
                "PERSON_GENDER_INSPECT_POSITION": (1180, 870, 1400, 955),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 865, 1520, 985)
            },
            OBRISTAN_COLOR: {
                "name": "Obristan",
                "DATE_POSITION": (2020, 1165),
                "PHOTO_POSITION": (2250, 1150),
                "CITY_POSITION": (1975, 1145),
                "GENDER_POSITION": (1958, 1111),
                "COUNTRY_POSITION": (1150, 780),

                "DATE_INSPECT_POSITION": (995, 1195, 1210, 1280),
                "CITY_INSPECT_POSITION": (1640, 1090, 1850, 1170),
                "PHOTO_GENDER_INSPECT_POSITION": (1870, 825, 2100, 900),
                "PERSON_GENDER_INSPECT_POSITION": (1185, 890, 1400, 970),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 900, 1510, 1002)
            },
            IMPOR_COLOR: {
                "name": "Impor",
                "DATE_POSITION": (2175, 1120),
                "PHOTO_POSITION": (1920, 1150),
                "CITY_POSITION": (2165, 1088),
                "GENDER_POSITION": (2128, 1054),
                "COUNTRY_POSITION": (1190, 1270),

                "DATE_INSPECT_POSITION": (1075, 1170, 1295, 1250),
                "CITY_INSPECT_POSITION": (1720, 1065, 1930, 1155),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 780, 2030, 870),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 860, 1495, 950),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 880, 1370, 970)
            },
            KOLECHIA_COLOR: {
                "name": "Kolechia",
                "DATE_POSITION": (2175, 1150),
                "PHOTO_POSITION": (1920, 1150),
                "CITY_POSITION": (2150, 1130),
                "GENDER_POSITION": (2128, 1095),
                "COUNTRY_POSITION": (1450, 810),

                "DATE_INSPECT_POSITION": (1075, 1190, 1295, 1270),
                "CITY_INSPECT_POSITION": (1740, 1085, 1950, 1175),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 815, 2020, 910),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 875, 1495, 969),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 910, 1370, 992)
            },
            UNITEDFED_COLOR: {
                "name": "UnitedFed",
                "DATE_POSITION": (2175, 1150),
                "PHOTO_POSITION": (1920, 1150),
                "CITY_POSITION": (2150, 1130),
                "GENDER_POSITION": (2128, 1095),
                "COUNTRY_POSITION": (900, 1220),

                "DATE_INSPECT_POSITION": (1075, 1180, 1295, 1270),
                "CITY_INSPECT_POSITION": (1720, 1075, 1950, 1195),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 825, 2020, 900),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 875, 1495, 969),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 900, 1400, 1000)
            },
            REPUBLIA_COLOR: {
                "name": "Republia",
                "DATE_POSITION": (2000, 1120),
                "PHOTO_POSITION": (2250, 1110),
                "CITY_POSITION": (1980, 1085),
                "GENDER_POSITION": (1962, 1055),
                "COUNTRY_POSITION": (1100, 1120),

                "DATE_INSPECT_POSITION": (995, 1165, 1212, 1270),
                "CITY_INSPECT_POSITION": (1650, 1070, 1860, 1150),
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
                DATE_INSPECT_POSITION = country_dict[color]["DATE_INSPECT_POSITION"]
                CITY_INSPECT_POSITION = country_dict[color]["CITY_INSPECT_POSITION"]
                PHOTO_GENDER_INSPECT_POSITION = country_dict[color]["PHOTO_GENDER_INSPECT_POSITION"]
                PERSON_GENDER_INSPECT_POSITION = country_dict[color]["PERSON_GENDER_INSPECT_POSITION"]
                PHOTO_PERSON_INSPECT_POSITION = country_dict[color]["PHOTO_PERSON_INSPECT_POSITION"]
                StampingTime = True
                break

        # Print the values of the variables for the matching country
        print(f" {name}!")

    # COMAPARE

    if StampingTime:
        # MOVE RULE
        drag_and_drop(RULE_BOOK_POSITION, RULE_BOOK_SLOT_POSITION)

        # CHECK CITY
        click_mouse(REGIONAL_MAP_POSITION)
        click_mouse(COUNTRY_POSITION)
        click_mouse(INSPECT_BUTTON_POSITION)
        click_mouse(CITY_POSITION)
        click_mouse(ISSUING_CITIES_POSITION)

        textdetect(CITY_INSPECT_POSITION, "City", CorrectCity)

        click_mouse(INSPECT_BUTTON_POSITION)

        # RULE BOOK BACK
        click_mouse(BOOKMARK_POSITION)

        drag_and_drop(RULE_BOOK_SLOT_POSITION, RULE_BOOK_POSITION)
