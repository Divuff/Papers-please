import time
import pydirectinput
import pyautogui
from PIL import ImageGrab


SpeakerX = 830
SpeakerY = 370

LeverX = 850
LeverY = 550

RuleBookSlotX = 1300
RuleBookSlotY = 1050

RuleBookX = 640
RuleBookY = 1250

PassportX = 550
PassportY = 1090

PassportSlotX = 2100
PassportSlotY = 950

TicketX = 500
TicketY = 1065

TicketSlotX = 1260
TicketSlotY = 625

TicketDateX = 1400
TicketDateY = 670

RegionalMapX = 1510
RegionalMapY = 970

InspectButtonX = 2350
InspectButtonY = 1320

IssuingCitiesX = 1400
IssuingCitiesY = 1120

PersonX = 470
PersonY = 900

DocumentDropX = 480
DocumentDropY = 730

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

DocumentHandOverX = 140
DocumentHandOverY = 535


# MOVE PASSPORT

pyautogui.moveTo(PassportX, PassportY)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(PassportSlotX, PassportSlotY)
time.sleep(0.03)
pyautogui.mouseUp(button='left')

pyautogui.moveTo(TicketX, TicketY)
pyautogui.mouseDown(button='left')
pyautogui.moveTo(TicketSlotX, TicketSlotY)
pyautogui.mouseUp(button='left')

