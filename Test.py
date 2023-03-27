import time
import pydirectinput
import pyautogui
from PIL import ImageGrab

# Constants
SPEAKER_POSITION = (830, 370)
LEVER_POSITION = (850, 550)
PASSPORT_POSITION = (475, 1085)
PASSPORT_SLOT_POSITION = (2100, 950)
ACCEPTED_PERSON_LEAVING_POSITION = (960, 450)
REJECTED_PERSON_LEAVING_POSITION = (700, 450)
DOCUMENT_DROP_POSITION = (480, 600)
DOCUMENT_AREA_POSITION = (500, 1080)
DAY_TEST_POSITION = (1444, 180)
PERSON_POSITION = (490, 850)
STAMP_TRAY_POSITION = (2400, 730)
APPROVAL_STAMP_POSITION = (2100, 730)
REJECTED_STAMP_POSITION = (1600, 695)
APPROVED_PASSPORT_POSITION = (2100, 950)
REJECTED_PASSPORT_POSITION = (1600, 950)
PASSPORT_BORDER_POSITION = (1845, 950)
TEXT_BOX_POSITION = (140, 535)

# Colors
ARSTOTZKA_COLOR = (0, 165, 255)
PERSON_COLOR = (235, 180, 90)
TEXTBOX_COLOR = (245, 245, 245)
DAY_COLOR = (70, 70, 70)
DOCUMENT_AREA_COLOR = (255, 255, 255)
DESK_COLOR = (115, 115, 115)
WALL_COLOR = (80, 80, 80)


# Functions
def get_image_color(position):
    color_detect = ImageGrab.grab().load()
    return color_detect[position[0], position[1]]


def move_mouse(position):
    pyautogui.moveTo(position)
    time.sleep(0.2)


def click_mouse(position):
    move_mouse(position)
    pyautogui.click()


def drag_and_drop(start_position, end_position):
    move_mouse(start_position)
    pyautogui.mouseDown(button='left')
    time.sleep(0.3)
    move_mouse(end_position)
    pyautogui.mouseUp(button='left')


def detect_person():
    return get_image_color(PERSON_POSITION) != WALL_COLOR


def detect_textbox():
    return get_image_color(TEXT_BOX_POSITION) == TEXTBOX_COLOR


def detect_passport():
    return get_image_color(DOCUMENT_AREA_POSITION) != DOCUMENT_AREA_COLOR


def detect_person_leaving():
    return get_image_color(ACCEPTED_PERSON_LEAVING_POSITION) == PERSON_COLOR or get_image_color(
        REJECTED_PERSON_LEAVING_POSITION) == PERSON_COLOR


def detect_country():
    return get_image_color(PASSPORT_BORDER_POSITION)


def accept_person():
    click_mouse(STAMP_TRAY_POSITION)
    click_mouse(APPROVAL_STAMP_POSITION)
    drag_and_drop(PASSPORT_SLOT_POSITION, DOCUMENT_DROP_POSITION)


def reject_person():
    click_mouse(STAMP_TRAY_POSITION)
    drag_and_drop(PASSPORT_SLOT_POSITION, REJECTED_PASSPORT_POSITION)
    click_mouse(REJECTED_STAMP_POSITION)
    drag_and_drop(REJECTED_PASSPORT_POSITION, DOCUMENT_DROP_POSITION)


def handle_no_passport():
    while not detect_person_leaving():
        pass


def handle_accepted_person():
    accept_person()
    while not detect_person_leaving():
        pass


def handle_rejected_person():
    reject_person()
    while not detect_person_leaving():
        pass


def handle_no_passport():
    while not detect_person_leaving():
        pass

    pyautogui.click(LEVER_POSITION)
    click_mouse(SPEAKER_POSITION)
    time.sleep(1)


while get_image_color(DAY_TEST_POSITION) == DAY_COLOR:
    if detect_person():
        if not detect_person_leaving():
            if detect_textbox:
                time.sleep(1.5)

                if not detect_passport():
                    drag_and_drop(PASSPORT_POSITION, PASSPORT_SLOT_POSITION)
                    print("Passport detected")
                else:
                    print("No passport!")
                    handle_no_passport()
            else:
                print("Textbox not detected")
        else:
            print("Person has left")
    else:
        print("No person detected")

    if detect_country() == ARSTOTZKA_COLOR:
        handle_accepted_person()
        print("Arstotzkan detected")
    elif detect_country() != DESK_COLOR:
        handle_rejected_person()
        print("Foreign scum")
    else:
        handle_no_passport()
        print("No passport")

    print("Day is over")

