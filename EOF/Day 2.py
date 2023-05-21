import time

import cv2
import pyautogui
import timer
from PIL import ImageGrab
import pytesseract
import numpy as nm
import Levenshtein

from Colors import Arstotzka, Obristan, Kolechia, Impor, UnitedFed, Republia, Antegria, black, LadyCard, LadyCardSecondary, PersonColor, TextBoxColor

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


DateX = ()
DateY = ()

CityX = ()
CityY = ()

GenderX = ()
GenderY = ()

PhotoX = ()
PhotoY = ()

CountryX = ()
CountryY = ()

DateInspectTopX = ()
DateInspectTopY = ()
DateInspectBottomX = ()
DateInspectBottomY = ()

CityInspectTopX = ()
CityInspectTopY = ()
CityInspectBottomX = ()
CityInspectBottomY = ()

PhotoGenderInspectTopX = ()
PhotoGenderInspectBottomX = ()
PhotoGenderInspectTopY = ()
PhotoGenderInspectBottomY = ()

PersonGenderInspectTopX = ()
PersonGenderInspectBottomX = ()
PersonGenderInspectTopY = ()
PersonGenderInspectBottomY = ()

PhotoPersonInspectTopX = ()
PhotoPersonInspectBottomX = ()
PhotoPersonInspectTopY = ()
PhotoPersonInspectBottomY = ()

SpeakerX = 830
SpeakerY = 370

LeverX = 850
LeverY = 550

RuleBookSlotX = 1300
RuleBookSlotY = 1050

RuleBookX = 640
RuleBookY = 1250

PassportX = 475
PassportY = 1085

PassportSlotX = 2100
PassportSlotY = 950

RegionalMapX = 1510
RegionalMapY = 970

InspectButtonX = 2350
InspectButtonY = 1320

IssuingCitiesX = 1400
IssuingCitiesY = 1120

PersonX = 490
PersonY = 850

DocumentDropX = 480
DocumentDropY = 600

DayTestX = 1444
DayTestY = 180

BookMarkX = 870
BookMarkY = 750

ClockX = 200
ClockY = 1320

AcceptedPersonLeavingX = 960
AcceptedPersonLeavingY = 450

RejectedPersonLeavingX = 700
RejectedPersonLeavingY = 450

RuleBookBasicsX = 1500
RuleBookBasicsY = 910

PassportRuleX = 1000
PassportRuleY = 850

InterrogateX = 500
InterrogateY = 1230

PassportBorderX = 1845
PassportBorderY = 950

TextBoxX = 140
TextBoxY = 535

DocumentAreaX = 500
DocumentAreaY = 1080

Matching = "MATCHING"
Date = ""
City = ""

day = (141, 141, 141)

dayStat = (141, 141, 141)

passport = (25, 18, 18)

desk = (25, 18, 18)

wall = (25, 18, 18)

wallStat = (25, 18, 18)

DocumentArea = (132, 138, 107)



PersonLeaving = ()

TextBox = ()
LadyWorker = ()


VisPassport = ()

# DaySTART
pyautogui.click(LeverX, LeverY)
pyautogui.click(SpeakerX, SpeakerY)
time.sleep(1)

while dayStat == day:

    # LADY DETECT
    lc = ImageGrab.grab().load()
    for y in range(PassportY, PassportY + 1):
        for x in range(PassportX, PassportX + 1):
            LadyWorker = lc[x, y]

    # TEXTBOX DETECT
    tb = ImageGrab.grab().load()
    for y in range(TextBoxY, TextBoxY + 1):
        for x in range(TextBoxX, TextBoxX + 1):
            TextBox = tb[x, y]

    # Day Stat
    py = ImageGrab.grab().load()
    for y in range(DayTestY, DayTestY + 1):
        for x in range(DayTestX, DayTestX + 1):
            dayStat = py[x, y]

    if wall != wallStat:
        wallStat = ()
        PersonPresent = True
        print("Person Detected")
    else:
        PersonPresent = False
        # Person Detect
        px = ImageGrab.grab().load()
        for y in range(PersonY, PersonY + 1):
            for x in range(PersonX, PersonX + 1):
                wallStat = px[x, y]




    if PersonLeaving != PersonColor:
        NextPerson = False
    else:
        NextPerson = True
        PersonLeaving = ()
        pyautogui.click(SpeakerX, SpeakerY)
        print("Ready for Next Person")

    if LadyWorker == LadyCard or LadyWorker == LadyCardSecondary:
        pyautogui.moveTo(PassportX, PassportY)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(PassportX - 300, PassportY)
        pyautogui.mouseUp(button='left')
        print("Lady Worker Card in the way!")

    if PersonPresent and TextBox == TextBoxColor:
        TextBoxPresent = True
        time.sleep(1.5)

        # VISUAL PASSPORT CHECK
        py = ImageGrab.grab().load()
        for y in range(DocumentAreaY, DocumentAreaY + 1):
            for x in range(DocumentAreaX, DocumentAreaX + 1):
                VisPassport = py[x, y]

        if VisPassport != DocumentArea:
            # MOVE PASSPORT
            pyautogui.moveTo(PassportX, PassportY)
            pyautogui.mouseDown(button='left')
            pyautogui.moveTo(PassportSlotX, PassportSlotY)
            pyautogui.mouseUp(button='left')

            VisPassportPresent = True
            print("Passport Detected")
        else:
            VisPassportPresent = False
            print("No Passport!")
    else:
        TextBoxPresent = False

    # PP Detect
    pp = ImageGrab.grab().load()
    for y in range(PassportBorderY, PassportBorderY + 1):
        for x in range(PassportBorderX, PassportBorderX + 1):
            passport = pp[x, y]


    if PersonPresent and VisPassportPresent and TextBoxPresent:
        # Define a dictionary to store the values for each country
        country_dict = {
            Arstotzka: {
                "name": "Arstotzka",
                "DateX": 2175,
                "DateY": 1120,
                "PhotoX": 1920,
                "PhotoY": 1120,
                "CityX": 2150,
                "CityY": 1090,
                "GenderX": 2128,
                "GenderY": 1060,
                "CountryX": 1650,
                "CountryY": 1080,
                "DateInspectTopX": 1070,
                "DateInspectBottomX": 1295,
                "DateInspectTopY": 1165,
                "DateInspectBottomY": 1255,
                "CityInspectTopX": 1740,
                "CityInspectBottomX": 1965,
                "CityInspectTopY": 1070,
                "CityInspectBottomY": 1160,
                "PhotoGenderInspectTopX": 1810,
                "PhotoGenderInspectBottomX": 2020,
                "PhotoGenderInspectTopY": 780,
                "PhotoGenderInspectBottomY": 870,
                "PersonGenderInspectTopX": 1260,
                "PersonGenderInspectBottomX": 1490,
                "PersonGenderInspectTopY": 865,
                "PersonGenderInspectBottomY": 955,
                "PhotoPersonInspectTopX": 1145,
                "PhotoPersonInspectBottomX": 1360,
                "PhotoPersonInspectTopY": 880,
                "PhotoPersonInspectBottomY": 970
            },
            Antegria: {
                "name": "Antegria",
                "DateX": 2020,
                "DateY": 1145,
                "PhotoX": 2255,
                "PhotoY": 1083,
                "CityX": 1987,
                "CityY": 1112,
                "GenderX": 1947,
                "GenderY": 1073,
                "CountryX": 1033,
                "CountryY": 952,
                "DateInspectTopX": 960,
                "DateInspectBottomX": 1240,
                "DateInspectTopY": 1170,
                "DateInspectBottomY": 1290,
                "CityInspectTopX": 1660,
                "CityInspectBottomX": 1870,
                "CityInspectTopY": 1080,
                "CityInspectBottomY": 1170,
                "PhotoGenderInspectTopX": 1870,
                "PhotoGenderInspectBottomX": 2085,
                "PhotoGenderInspectTopY": 745,
                "PhotoGenderInspectBottomY": 825,
                "PersonGenderInspectTopX": 1180,
                "PersonGenderInspectBottomX": 1400,
                "PersonGenderInspectTopY": 870,
                "PersonGenderInspectBottomY": 955,
                "PhotoPersonInspectTopX": 1300,
                "PhotoPersonInspectBottomX": 1520,
                "PhotoPersonInspectTopY": 865,
                "PhotoPersonInspectBottomY": 985

            },
            Obristan: {
                "name": "Obristan",
                "DateX": 2020,
                "DateY": 1165,
                "PhotoX": 2250,
                "PhotoY": 1150,
                "CityX": 1975,
                "CityY": 1145,
                "GenderX": 1958,
                "GenderY": 1111,
                "CountryX": 1150,
                "CountryY": 780,
                "DateInspectTopX": 995,
                "DateInspectBottomX": 1210,
                "DateInspectTopY": 1195,
                "DateInspectBottomY": 1280,
                "CityInspectTopX": 1640,
                "CityInspectBottomX": 1850,
                "CityInspectTopY": 1090,
                "CityInspectBottomY": 1170,
                "PhotoGenderInspectTopX": 1870,
                "PhotoGenderInspectBottomX": 2100,
                "PhotoGenderInspectTopY": 825,
                "PhotoGenderInspectBottomY": 900,
                "PersonGenderInspectTopX": 1185,
                "PersonGenderInspectBottomX": 1400,
                "PersonGenderInspectTopY": 890,
                "PersonGenderInspectBottomY": 970,
                "PhotoPersonInspectTopX": 1300,
                "PhotoPersonInspectBottomX": 1510,
                "PhotoPersonInspectTopY": 900,
                "PhotoPersonInspectBottomY": 1002

            },
            Impor: {
                "name": "Impor",
                "DateX": 2175,
                "DateY": 1120,
                "PhotoX": 1920,
                "PhotoY": 1150,
                "CityX": 2165,
                "CityY": 1088,
                "GenderX": 2128,
                "GenderY": 1054,
                "CountryX": 1190,
                "CountryY": 1270,
                "DateInspectTopX": 1075,
                "DateInspectBottomX": 1295,
                "DateInspectTopY": 1170,
                "DateInspectBottomY": 1250,
                "CityInspectTopX": 1720,
                "CityInspectBottomX": 1930,
                "CityInspectTopY": 1065,
                "CityInspectBottomY": 1155,
                "PhotoGenderInspectTopX": 1810,
                "PhotoGenderInspectBottomX": 2030,
                "PhotoGenderInspectTopY": 780,
                "PhotoGenderInspectBottomY": 870,
                "PersonGenderInspectTopX": 1260,
                "PersonGenderInspectBottomX": 1495,
                "PersonGenderInspectTopY": 860,
                "PersonGenderInspectBottomY": 950,
                "PhotoPersonInspectTopX": 1150,
                "PhotoPersonInspectBottomX": 1370,
                "PhotoPersonInspectTopY": 880,
                "PhotoPersonInspectBottomY": 970
            },
            Kolechia: {
                "name": "Kolechia",
                "DateX": 2175,
                "DateY": 1150,
                "PhotoX": 1920,
                "PhotoY": 1150,
                "CityX": 2150,
                "CityY": 1130,
                "GenderX": 2128,
                "GenderY": 1095,
                "CountryX": 1450,
                "CountryY": 810,
                "DateInspectTopX": 1075,
                "DateInspectBottomX": 1295,
                "DateInspectTopY": 1190,
                "DateInspectBottomY": 1270,
                "CityInspectTopX": 1740,
                "CityInspectBottomX": 1950,
                "CityInspectTopY": 1085,
                "CityInspectBottomY": 1175,
                "PhotoGenderInspectTopX": 1810,
                "PhotoGenderInspectBottomX": 2020,
                "PhotoGenderInspectTopY": 815,
                "PhotoGenderInspectBottomY": 910,
                "PersonGenderInspectTopX": 1260,
                "PersonGenderInspectBottomX": 1495,
                "PersonGenderInspectTopY": 875,
                "PersonGenderInspectBottomY": 969,
                "PhotoPersonInspectTopX": 1150,
                "PhotoPersonInspectBottomX": 1370,
                "PhotoPersonInspectTopY": 910,
                "PhotoPersonInspectBottomY": 992
            },
            UnitedFed: {
                "name": "UnitedFed",
                "DateX": 2175,
                "DateY": 1150,
                "PhotoX": 1920,
                "PhotoY": 1150,
                "CityX": 2150,
                "CityY": 1130,
                "GenderX": 2128,
                "GenderY": 1095,
                "CountryX": 900,
                "CountryY": 1220,
                "DateInspectTopX": 1075,
                "DateInspectBottomX": 1295,
                "DateInspectTopY": 1180,
                "DateInspectBottomY": 1270,
                "CityInspectTopX": 1720,
                "CityInspectBottomX": 1950,
                "CityInspectTopY": 1075,
                "CityInspectBottomY": 1195,
                "PhotoGenderInspectTopX": 1810,
                "PhotoGenderInspectBottomX": 2020,
                "PhotoGenderInspectTopY": 825,
                "PhotoGenderInspectBottomY": 900,
                "PersonGenderInspectTopX": 1260,
                "PersonGenderInspectBottomX": 1495,
                "PersonGenderInspectTopY": 875,
                "PersonGenderInspectBottomY": 969,
                "PhotoPersonInspectTopX": 1150,
                "PhotoPersonInspectBottomX": 1400,
                "PhotoPersonInspectTopY": 900,
                "PhotoPersonInspectBottomY": 1000
            },
            Republia: {
                "name": "Republia",
                "DateX": 2000,
                "DateY": 1120,
                "PhotoX": 2250,
                "PhotoY": 1110,
                "CityX": 1980,
                "CityY": 1085,
                "GenderX": 1962,
                "GenderY": 1055,
                "CountryX": 1100,
                "CountryY": 1120,
                "DateInspectTopX": 995,
                "DateInspectBottomX": 1212,
                "DateInspectTopY": 1165,
                "DateInspectBottomY": 1270,
                "CityInspectTopX": 1650,
                "CityInspectBottomX": 1860,
                "CityInspectTopY": 1070,
                "CityInspectBottomY": 1150,
                "PhotoGenderInspectTopX": 1875,
                "PhotoGenderInspectBottomX": 2100,
                "PhotoGenderInspectTopY": 770,
                "PhotoGenderInspectBottomY": 850,
                "PersonGenderInspectTopX": 1185,
                "PersonGenderInspectBottomX": 1410,
                "PersonGenderInspectTopY": 860,
                "PersonGenderInspectBottomY": 950,
                "PhotoPersonInspectTopX": 1300,
                "PhotoPersonInspectBottomX": 1520,
                "PhotoPersonInspectTopY": 880,
                "PhotoPersonInspectBottomY": 970
            }
        }

        # Find the matching country in the dictionary
        for color in country_dict:
            if passport == color:
                matching_country = country_dict[color]["name"]
                break

        # Assign the variables based on the matching country
        for color in country_dict:
            if country_dict[color]["name"] == matching_country:
                name = country_dict[color]["name"]
                DateX = country_dict[color]["DateX"]
                DateY = country_dict[color]["DateY"]
                PhotoX = country_dict[color]["PhotoX"]
                PhotoY = country_dict[color]["PhotoY"]
                CityX = country_dict[color]["CityX"]
                CityY = country_dict[color]["CityY"]
                GenderX = country_dict[color]["GenderX"]
                GenderY = country_dict[color]["GenderY"]
                CountryX = country_dict[color]["CountryX"]
                CountryY = country_dict[color]["CountryY"]
                DateInspectTopX = country_dict[color]["DateInspectTopX"]
                DateInspectBottomX = country_dict[color]["DateInspectBottomX"]
                DateInspectTopY = country_dict[color]["DateInspectTopY"]
                DateInspectBottomY = country_dict[color]["DateInspectBottomY"]
                CityInspectTopX = country_dict[color]["CityInspectTopX"]
                CityInspectBottomX = country_dict[color]["CityInspectBottomX"]
                CityInspectTopY = country_dict[color]["CityInspectTopY"]
                CityInspectBottomY = country_dict[color]["CityInspectBottomY"]
                PhotoGenderInspectTopX = country_dict[color]["PhotoGenderInspectTopX"]
                PhotoGenderInspectBottomX = country_dict[color]["PhotoGenderInspectBottomX"]
                PhotoGenderInspectTopY = country_dict[color]["PhotoGenderInspectTopY"]
                PhotoGenderInspectBottomY = country_dict[color]["PhotoGenderInspectBottomY"]
                PersonGenderInspectTopX = country_dict[color]["PersonGenderInspectTopX"]
                PersonGenderInspectBottomX = country_dict[color]["PersonGenderInspectBottomX"]
                PersonGenderInspectTopY = country_dict[color]["PersonGenderInspectTopY"]
                PersonGenderInspectBottomY = country_dict[color]["PersonGenderInspectBottomY"]
                PhotoPersonInspectTopX = country_dict[color]["PhotoPersonInspectTopX"]
                PhotoPersonInspectBottomX = country_dict[color]["PhotoPersonInspectBottomX"]
                PhotoPersonInspectTopY = country_dict[color]["PhotoPersonInspectTopY"]
                PhotoPersonInspectBottomY = country_dict[color]["PhotoPersonInspectBottomY"]
                StampingTime = True
                break

        # Print the values of the variables for the matching country
        print(f"The variables for {matching_country} are:")
        print(f" {name}")




    # COMAPARE

    if StampingTime:
        # MOVE RULE
        pyautogui.moveTo(RuleBookX, RuleBookY)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(RuleBookSlotX, RuleBookSlotY)
        pyautogui.mouseUp(button='left')

        # CHECK CITY
        pyautogui.moveTo(RegionalMapX, RegionalMapY)
        time.sleep(0.1)
        pyautogui.click()

        pyautogui.moveTo(CountryX, CountryY)
        time.sleep(0.1)
        pyautogui.click()

        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

        pyautogui.moveTo(CityX, CityY)

        pyautogui.click()

        pyautogui.moveTo(IssuingCitiesX, IssuingCitiesY)
        pyautogui.click()

        # Path of tesseract executable
        time.sleep(2)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        cap = ImageGrab.grab(bbox=(CityInspectTopX, CityInspectTopY, CityInspectBottomX, CityInspectBottomY))

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

        pyautogui.moveTo(InspectButtonX, InspectButtonY)
        pyautogui.click()

        # RULE BOOK BACK
        pyautogui.moveTo(BookMarkX, BookMarkY)
        pyautogui.click()

        pyautogui.moveTo(RuleBookSlotX, RuleBookSlotY)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(RuleBookX, RuleBookY)
        pyautogui.mouseUp(button='left')

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
            bbox=(PersonGenderInspectTopX, PersonGenderInspectTopY, PersonGenderInspectBottomX, PersonGenderInspectBottomY))

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

