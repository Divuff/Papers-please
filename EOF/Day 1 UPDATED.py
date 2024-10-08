import time
import pyautogui
from PIL import ImageGrab

from Colors import ARSTOTZKA_COLOR, PERSON_COLOR, TEXTBOX_COLOR, DAY_COLOR, DOCUMENT_AREA_COLOR, WALL_COLOR

# Positions
TEXT_BOX_POSITION = (140, 535)
PASSPORT_SIDE_POSITION = (175, 1085)
CLOCK_POSITION = (200, 1320)

PASSPORT_POSITION = (475, 1085)
DOCUMENT_DROP_POSITION = (480, 600)
PERSON_POSITION = (490, 850)
INTERROGATE_POSITION = (500, 1230)
DOCUMENT_AREA_POSITION = (500, 1080)

RULE_BOOK_POSITION = (640, 1250)
REJECTED_PERSON_LEAVING_POSITION = (700, 430)
SPEAKER_POSITION = (830, 370)

LEVER_POSITION = (850, 550)
BOOKMARK_POSITION = (870, 750)
ACCEPTED_PERSON_LEAVING_POSITION = (960, 430)

PASSPORT_RULE_POSITION = (1000, 850)


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

# Logic Variables
PersonPresent = False
PassportPresent = False
Arstotzkan = False
StampingTime = False
NoPassport = False


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
    print("FOREIGN SCUM")
    click_mouse(STAMP_TRAY_POSITION)
    time.sleep(0.3)
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


# Main program
pyautogui.click(LEVER_POSITION)
click_mouse(SPEAKER_POSITION)
time.sleep(1)

person_leaving_area = ()
while get_image_color(DAY_TEST_POSITION) == DAY_COLOR:


    # Person Leaving Booth Check
    if person_leaving_area != PERSON_COLOR:
        NextPerson = False
    else:
        NextPerson = True
        PersonLeaving = ()
        pyautogui.click(SpeakerX, SpeakerY)
        print("Ready for Next Person")


    # Check if person is present
    person_area = get_image_color(PERSON_POSITION)
    if person_area != WALL_COLOR:
        if not PersonPresent:
            PersonPresent = True
            print("Person Detected")

    else:
        PersonPresent = False

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


    country = get_image_color(PASSPORT_BORDER_POSITION)


    if country == ARSTOTZKA_COLOR:
        Arstotzkan = True
        print("Arstotzkan Detected")

    if PersonPresent and PassportPresent:
        StampingTime = True

        # APPROVAL STAMP
        if StampingTime and Arstotzkan:
            approve_passport()
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(ACCEPTED_PERSON_LEAVING_POSITION)


        # REJECTED STAMP
        elif StampingTime:
            reject_passport()
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)
    # NO PASSPORT
    if NoPassport:
        reset_person()
        while person_leaving_area != PERSON_COLOR:
            person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)






