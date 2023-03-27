import time

import cv2
import pyautogui
import timer
from PIL import ImageGrab
import pytesseract
import numpy as nm
import Levenshtein

from Colors import Arstotzka, Obristan, Kolechia, Impor, UnitedFed, Republia, Antegria, black, LadyCard, \
    LadyCardSecondary, PersonColor, TextBoxColor

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
    click_mouse(STAMP_TRAY_POSTITION)
    click_mouse(APPROVAL_STAMP_POSITION)
    drag_and_drop(PASSPORT_SLOT_POSITION, DOCUMENT_DROP_POSITION)


def reject_passport():
    print("FOREIGN SCUM")
    click_mouse(STAMP_TRAY_POSTITION)
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

    lady_card_area = get_image_color(PASSPORT_POSITION)
    if LadyWorker == LadyCard or LadyWorker == LadyCardSecondary:
        move_intrusive_object()
        print("Lady Worker Card in the way!")

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
            Arstotzka: {
                "name": "Arstotzka",
                "DATE_POSITION": (2175, 1120),
                "PHOTO_POSITION": (1920, 1120),
                "CITY_POSITION": (2150, 1090),
                "GENDER_POSITION": (2128, 1060),
                "COUNTRY_POSITION": (1650, 1080),

                "DATE_INSPECT_POSITION": (1070, 1295, 1165, 1255),
                "CITY_INSPECT_POSITION": (1740, 1965, 1070, 1160),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 2020, 780, 870),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 1490, 865, 955),
                "PHOTO_PERSON_INSPECT_POSITION": (1145, 1360, 880, 970)
            },
            Antegria: {
                "name": "Antegria",
                "DATE_POSITION": (2020, 1145),
                "PHOTO_POSITION": (2255, 1083),
                "CITY_POSITION": (1987, 1112),
                "GENDER_POSITION": (1947, 1073),
                "COUNTRY_POSITION": (1033, 952),
                "DATE_INSPECT_POSITION": (960, 1240, 1170, 1290),
                "CITY_INSPECT_POSITION": (1660, 1870, 1080, 1170),
                "PHOTO_GENDER_INSPECT_POSITION": (1870, 2085, 745, 825),
                "PERSON_GENDER_INSPECT_POSITION": (1180, 1400, 870, 955),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 1520, 865, 985)
            },
            Obristan: {
                "name": "Obristan",
                "DATE_POSITION": (2020, 1165),
                "PHOTO_POSITION": (2250, 1150),
                "CITY_POSITION": (1975, 1145),
                "GENDER_POSITION": (1958, 1111),
                "COUNTRY_POSITION": (1150, 780),
                "DATE_INSPECT_POSITION": (995, 1210, 1195, 1280),
                "CITY_INSPECT_POSITION": (1640, 1850, 1090, 1170),
                "PHOTO_GENDER_INSPECT_POSITION": (1870, 2100, 825, 900),
                "PERSON_GENDER_INSPECT_POSITION": (1185, 1400, 890, 970),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 1510, 900, 1002)
            },
            Impor: {
                "name": "Impor",
                "DATE_POSITION": (2175, 1120),
                "PHOTO_POSITION": (1920, 1150),
                "CITY_POSITION": (2165, 1088),
                "GENDER_POSITION": (2128, 1054),
                "COUNTRY_POSITION": (1190, 1270),

                "DATE_INSPECT_POSITION": (1075, 1295, 1170, 1250),
                "CITY_INSPECT_POSITION": (1720, 1930, 1065, 1155),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 2030, 780, 870),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 1495, 860, 950),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 1370, 880, 970)
            },
            Kolechia: {
                "name": "Kolechia",
                "DATE_POSITION": (2175, 1150),
                "PHOTO_POSITION": (1920, 1150),
                "CITY_POSITION": (2150, 1130),
                "GENDER_POSITION": (2128, 1095),
                "COUNTRY_POSITION": (1450, 810),

                "DATE_INSPECT_POSITION": (1075, 1295, 1190, 1270),
                "CITY_INSPECT_POSITION": (1740, 1950, 1085, 1175),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 2020, 815, 910),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 1495, 875, 969),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 1370, 910, 992)
            },
            UnitedFed: {
                "name": "UnitedFed",
                "DATE_POSITION": (2175, 1150),
                "PHOTO_POSITION": (1920, 1150),
                "CITY_POSITION": (2150, 1130),
                "GENDER_POSITION": (2128, 1095),
                "COUNTRY_POSITION": (900, 1220),

                "DATE_INSPECT_POSITION": (1075, 1295, 1180, 1270),
                "CITY_INSPECT_POSITION": (1720, 1950, 1075, 1195),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 2020, 825, 900),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 1495, 875, 969),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 1400, 900, 1000)
            },
            Republia: {
                "name": "Republia",
                "DATE_POSITION": (2000, 1120),
                "PHOTO_POSITION": (2250, 1110),
                "CITY_POSITION": (1980, 1085),
                "GENDER_POSITION": (1962, 1055),
                "COUNTRY_POSITION": (1100, 1120),

                "DATE_INSPECT_POSITION": (995, 1212, 1165, 1270),
                "CITY_INSPECT_POSITION": (1650, 1860, 1070, 1150),
                "PHOTO_GENDER_INSPECT_POSITION": (1875, 2100, 770, 850),
                "PERSON_GENDER_INSPECT_POSITION": (1185, 1410, 860, 950),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 1520, 880, 970)
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
        print(f"The variables for {matching_country} are:")
        print(f" {name}")

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

        # Path of tesseract executable
        time.sleep(2)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        cap = ImageGrab.grab(bbox=CITY_INSPECT_POSITION)

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        City = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')

        City = City.strip()
        print(City)

        similarity_ratio = Levenshtein.ratio(City, Matching)
        if similarity_ratio >= 0.75:
            print("City Match!")
            CorrectCity = True
        else:
            CorrectCity = False
            print("Incorrect City!")

        click_mouse(INSPECT_BUTTON_POSITION)

        # RULE BOOK BACK
        click_mouse(BOOKMARK_POSITION)

        drag_and_drop(RULE_BOOK_SLOT_POSITION, RULE_BOOK_POSITION)

    if CorrectCity:

        # CHECK DATE
        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

        pyautogui.moveTo(DateX, DateY)
        pyautogui.click()
        pyautogui.moveTo(ClockX, ClockY)
        pyautogui.click()

        # Path of tesseract executable
        time.sleep(2)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        cap = ImageGrab.grab(bbox=(DateInspectTopX, DateInspectTopY, DateInspectBottomX, DateInspectBottomY))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        Date = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')

        Date = Date.strip()
        print(Date)

        similarity_ratio = Levenshtein.ratio(Date, Matching)
        if similarity_ratio >= 0.75:
            CorrectDate = True
            print("Dates Match!")
        else:
            CorrectDate = False
            print("Incorrect Dates!")

        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

    if CorrectDate:
        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

        # CHECK GENDER WITH PHOTO
        pyautogui.moveTo(PhotoX, PhotoY)

        pyautogui.click()

        pyautogui.moveTo(GenderX, GenderY)

        pyautogui.click()

        # Path of tesseract executable
        time.sleep(3)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        cap = ImageGrab.grab(
            bbox=(PhotoGenderInspectTopX, PhotoGenderInspectTopY, PhotoGenderInspectBottomX, PhotoGenderInspectBottomY))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        PhotoGenderMatch = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')

        PhotoGenderMatch = PhotoGenderMatch.strip()
        print(PhotoGenderMatch)

        similarity_ratio = Levenshtein.ratio(PhotoGenderMatch, Matching)
        if similarity_ratio >= 0.75:
            PhotoGenderMatch = True
            print("Gender Matches Passport!")
        else:
            PhotoGenderMatch = False
            print("Gender Doesn't Match Passport!")

        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

    if PhotoGenderMatch:
        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

        # CHECK GENDER WITH Person
        pyautogui.moveTo(PersonX, PersonY)
        pyautogui.click()

        pyautogui.moveTo(GenderX, GenderY)
        pyautogui.click()

        # Path of tesseract executable
        time.sleep(2)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        cap = ImageGrab.grab(
            bbox=(
            PersonGenderInspectTopX, PersonGenderInspectTopY, PersonGenderInspectBottomX, PersonGenderInspectBottomY))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        PersonGenderMatch = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')

        PersonGenderMatch = PersonGenderMatch.strip()
        print(PersonGenderMatch)

        similarity_ratio = Levenshtein.ratio(PersonGenderMatch, Matching)
        if similarity_ratio >= 0.75:
            PersonGenderMatch = True
            print("Correct Gender!")
        else:
            PersonGenderMatch = False
            print("Incorrect Gender!")

        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

    if PersonGenderMatch:
        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

        # CHECK PERSON WITH PHOTO
        pyautogui.moveTo(PersonX, PersonY)
        pyautogui.click()

        pyautogui.moveTo(PhotoX, PhotoY)
        time.sleep(1)
        pyautogui.click()

        # Path of tesseract executable
        time.sleep(2)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        cap = ImageGrab.grab(
            bbox=(PhotoPersonInspectTopX, PhotoPersonInspectTopY, PhotoPersonInspectBottomX, PhotoPersonInspectBottomY))

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        PhotoPersonMatch = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')

        PhotoPersonMatch = PhotoPersonMatch.strip()
        print(PhotoPersonMatch)

        similarity_ratio = Levenshtein.ratio(PhotoPersonMatch, Matching)
        if similarity_ratio >= 0.75:
            PhotoPersonMatch = True
            print("Correct Photo!")
        else:
            PhotoPersonMatch = False
            print("Incorrect Photo!")

        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

    if PhotoPersonMatch:
        print("WELCOME!")
        pyautogui.moveTo(2400, 730)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.moveTo(2100, 730)
        pyautogui.click()
        pyautogui.moveTo(2100, 950)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(480, 730)
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(1320, 730)
        pyautogui.click()

        PersonPresent = False
        PassportPresent = False
        PhotoPersonMatch = False
        PersonGenderMatch = False
        PhotoGenderMatch = False
        CorrectDate = False
        CorrectCity = False
        StampingTime = False
        NextPerson = False
        PersonLeaving = False
        TextBoxPresent = False
        VisPassportPresent = False

        VisPassport = ()
        PersonLeaving = ()
        TextBox = ()
        wallStat = ()
        LadyWorker = ()
        wallStat = (25, 18, 18)

        while PersonLeaving != PersonColor:
            # Accepted Person Leaving Detect
            apl = ImageGrab.grab().load()
            for y in range(AcceptedPersonLeavingY, AcceptedPersonLeavingY + 1):
                for x in range(AcceptedPersonLeavingX, AcceptedPersonLeavingX + 1):
                    PersonLeaving = apl[x, y]
    elif StampingTime:
        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

        pyautogui.moveTo(2101, 800)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(1800, 800)
        pyautogui.mouseUp(button='left')
        pyautogui.click(2400, 750)
        time.sleep(1)
        pyautogui.click(1500, 695)
        pyautogui.moveTo(1600, 1000)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(DocumentDropX, DocumentDropY)
        pyautogui.mouseUp(button='left')

        PersonPresent = False
        PassportPresent = False
        PhotoPersonMatch = False
        PersonGenderMatch = False
        PhotoGenderMatch = False
        CorrectDate = False
        CorrectCity = False
        StampingTime = False
        NextPerson = False
        PersonLeaving = False
        TextBoxPresent = False
        VisPassportPresent = False

        VisPassport = ()
        PersonLeaving = ()
        TextBox = ()
        wallStat = ()
        LadyWorker = ()
        wallStat = (25, 18, 18)

        while PersonLeaving != PersonColor:
            # Rejected Person Leaving Detect
            rpl = ImageGrab.grab().load()
            for y in range(RejectedPersonLeavingY, RejectedPersonLeavingY + 1):
                for x in range(RejectedPersonLeavingX, RejectedPersonLeavingX + 1):
                    PersonLeaving = rpl[x, y]
