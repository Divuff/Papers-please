import time

import cv2
import pyautogui
from PIL import ImageGrab
import pytesseract
import numpy as nm
import Levenshtein

from Colors import ARSTOTZKA_COLOR, PERSON_COLOR, TEXTBOX_COLOR, DAY_COLOR, DOCUMENT_AREA_COLOR, DESK_COLOR, WALL_COLOR, \
    ANTEGRIA_COLOR, OBRISTAN_COLOR, UNITEDFED_COLOR, REPUBLIA_COLOR, IMPOR_COLOR, KOLECHIA_COLOR, LadyCard, LadyCardSecondary

country = IMPOR_COLOR
Matching = "MATCHING"
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
                "CITY_INSPECT_POSITION": (1550, 850, 1860, 950),
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



def textdetect(inspect_position):
    # Path of tesseract executable
    time.sleep(2)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Converted the image to monochrome for it to be easily
    # read by the OCR and obtained the output String.
    text = pytesseract.image_to_string(
        cv2.cvtColor(nm.array(ImageGrab.grab(bbox=inspect_position)), cv2.COLOR_BGR2GRAY),
        lang='eng')

    text = text.strip()
    print(text)
    if Levenshtein.ratio(text, Matching) >= 0.75:
        print(text, "Match!")
        return True
    else:
        print("Incorrect", text, "!")
        return False


CorrectCity = textdetect(CITY_INSPECT_POSITION)
