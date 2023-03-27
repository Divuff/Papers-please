import time
import pydirectinput
import pyautogui
from PIL import ImageGrab
from Colors import Arstotzka, PersonColor, TextBoxColor

# Logic Variables
PersonPresent = False
PassportPresent = False
Arstotzkan = False
StampingTime = False
NoPassport = False
VisPassportPresent = False
Checks = 0

SpeakerX = 830
SpeakerY = 370

LeverX = 850
LeverY = 550

PassportX = 475
PassportY = 1085
PassportSlotX = 2100
PassportSlotY = 950

AcceptedPersonLeavingX = 960
AcceptedPersonLeavingY = 450

RejectedPersonLeavingX = 700
RejectedPersonLeavingY = 450

PassportBorderX = 1845

PassportBorderY = 950

TextBoxX = 140
TextBoxY = 535

DayTestX = 1444
DayTestY = 180

PersonX = 490
PersonY = 850

AcceptedPersonLeavingX = 960
AcceptedPersonLeavingY = 450

RejectedPersonLeavingX = 700
RejectedPersonLeavingY = 450

DocumentDropX = 480
DocumentDropY = 600

DocumentAreaX = 500
DocumentAreaY = 1080

day = (141, 141, 141)

dayStat = (141, 141, 141)

passport = (25, 18, 18)

desk = (25, 18, 18)

wall = (25, 18, 18)

wallStat = (25, 18, 18)

DocumentArea = (132, 138, 107)

PersonLeaving = ()

TextBox = ()

# Starts the game
pyautogui.click(LeverX, LeverY)
pyautogui.click(SpeakerX, SpeakerY)
time.sleep(1)

# Check to see if day is over
while dayStat == day:

    # TEXTBOX DETECT
    tb = ImageGrab.grab().load()
    for y in range(TextBoxY, TextBoxY + 1):
        for x in range(TextBoxX, TextBoxX + 1):
            TextBox = tb[x, y]

    # DAY STATUS DETECT
    py = ImageGrab.grab().load()
    for y in range(DayTestY, DayTestY + 1):
        for x in range(DayTestX, DayTestX + 1):
            dayStat = py[x, y]

    # Person DETECT
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

    # Person Leaving Booth Check
    if PersonLeaving != PersonColor:
        NextPerson = False
    else:
        NextPerson = True
        PersonLeaving = ()
        pyautogui.click(SpeakerX, SpeakerY)
        print("Ready for Next Person")

    # Check for Person and text box
    if PersonPresent and TextBox == TextBoxColor:
        TextBoxPresent = True
        time.sleep(1.5)

        # PASSPORT CHECK
        py = ImageGrab.grab().load()
        for y in range(DocumentAreaY, DocumentAreaY + 1):
            for x in range(DocumentAreaX, DocumentAreaX + 1):
                VisPassport = py[x, y]



    # COUNTRY DETECT
    pp = ImageGrab.grab().load()
    for y in range(PassportBorderY, PassportBorderY + 1):
        for x in range(PassportBorderX, PassportBorderX + 1):
            country = pp[x, y]


    # CHECKS IF PASSPORT IS FOR ARSTOTZKA
    if country == Arstotzka:
        Arstotzkan = True
        print("Arstotzkan Detected")

    if PersonPresent and VisPassportPresent:
        StampingTime = True

    #APPROVAL STAMP
    if StampingTime and Arstotzkan:
        print("WELCOME!")
        pyautogui.moveTo(2400, 730)
        pyautogui.click()
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
        Arstotzkan = False
        StampingTime = False
        VisPassportPresent = False
        NoPassport = False

        VisPassport = ()
        PersonLeaving = ()
        TextBox = ()
        wallStat = ()

        wallStat = (25, 18, 18)

        while PersonLeaving != PersonColor:
            # Rejected Person Leaving Detect
            rpl = ImageGrab.grab().load()
            for y in range(AcceptedPersonLeavingY, AcceptedPersonLeavingY + 1):
                for x in range(AcceptedPersonLeavingX, AcceptedPersonLeavingX + 1):
                    PersonLeaving = rpl[x, y]

    #REJECTED STAMP
    elif StampingTime:
        print("FOREIGN SCUM")
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
        Arstotzkan = False
        StampingTime = False
        VisPassportPresent = False
        NoPassport = False

        VisPassport = ()
        PersonLeaving = ()
        TextBox = ()
        wallStat = ()

        wallStat = (25, 18, 18)

        while PersonLeaving != PersonColor:
            # Rejected Person Leaving Detect
            rpl = ImageGrab.grab().load()
            for y in range(RejectedPersonLeavingY, RejectedPersonLeavingY + 1):
                for x in range(RejectedPersonLeavingX, RejectedPersonLeavingX + 1):
                    PersonLeaving = rpl[x, y]

    #NO PASSPORT
    elif NoPassport:
        PersonPresent = False
        PassportPresent = False
        Arstotzkan = False
        StampingTime = False
        VisPassportPresent = False
        NoPassport = False

        VisPassport = ()
        PersonLeaving = ()
        TextBox = ()
        wallStat = ()

        wallStat = (25, 18, 18)

        while PersonLeaving != PersonColor:
            # Rejected Person Leaving Detect
            rpl = ImageGrab.grab().load()
            for y in range(RejectedPersonLeavingY, RejectedPersonLeavingY + 1):
                for x in range(RejectedPersonLeavingX, RejectedPersonLeavingX + 1):
                    PersonLeaving = rpl[x, y]


