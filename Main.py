import time
import pydirectinput
import pyautogui
from PIL import ImageGrab

EXT_BOX_POSITION = (95, 535)

PASSPORT_POSITION = (430, 1085)
DOCUMENT_DROP_POSITION = (435, 600)
PERSON_POSITION = (445, 850)

DOCUMENT_AREA_POSITION = (455, 1080)

REJECTED_PERSON_LEAVING_POSITION = (655, 450)
SPEAKER_POSITION = (785, 345)
LEVER_POSITION = (805, 550)

ACCEPTED_PERSON_LEAVING_POSITION = (915, 450)

DAY_TEST_POSITION = (1569, 180)

REJECTED_STAMP_POSITION = (1725, 695)
REJECTED_PASSPORT_POSITION = (1725, 1070)
PASSPORT_BORDER_POSITION = (1970, 1070)
PASSPORT_SLOT_POSITION = (2225, 1070)
APPROVAL_STAMP_POSITION = (2225, 730)
APPROVED_PASSPORT_POSITION = (2225, 1070)

STAMP_TRAY_POSITION = (2525, 730)


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

# MOVE PASSPORT

drag_and_drop(PASSPORT_POSITION, PASSPORT_SLOT_POSITION)

# MOVE RULE
drag_and_drop(RULE_BOOK_POSITION, RULE_BOOK_SLOT_POSITION)