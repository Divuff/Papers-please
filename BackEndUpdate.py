import os
import time
from datetime import datetime

import cv2
import numpy as np
import pyautogui
from Levenshtein import ratio
from PIL import ImageGrab
from google.cloud import vision

import Logic
from Text_Detection import *
from Pos import positions, country_dict
from Colors import ENTRY_PERMIT_COLOR, TEXTBOX_COLOR, DOCUMENT_AREA_COLOR, TICKET_COLOR, TICKET_COLOR2, PERSON_COLOR
from Text_Detection import word_search


# Define the purpose_data tuple
purpose_data = [
    ("immigrate", [
        "immigrating ",
        "live with ",
        "i will move "
    ]),
    ("visit", [
        "visit ",
        "visiting"
    ]),
    ("transit", [
        "transit ",
        "passing through"
    ])
]


time_length_data = (
    ("2 days", {"2 days", "two days", "48 hours", "forty-eight hours", "couple days", "a couple of days"}),
    ("1 week", {"1 week", "one week", "7 days", "seven days", "a week"}),
    ("14 days", {"14 days", "two weeks", "2 weeks", "couple of weeks", "couple weeks", "a couple of weeks"}),
    ("1 month", {"1 month", "one month", "30 days", "thirty days", "4 weeks", "four weeks"}),
    ("2 months", {"2 months", "two months", "8 weeks", "eight weeks", "a couple of months"}),
    ("3 months", {"3 months", "three months", "90 days", "ninety days", "12 weeks", "twelve weeks", "a few months"}),
    ("6 months", {"6 months", "six months", "180 days", "one hundred eighty days", "half a year"}),
    ("1 year", {"1 year", "one year", "365 days", "three hundred sixty-five days", "twelve months"}),
    ("forever", {"forever", "immigrating", "live with", "i will move"})
)

Matching = "MATCHING"

# Initialize the Google Vision client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/dunke/Downloads/papers-please-382221-ee7f3abe8cd7.json'
client = vision.ImageAnnotatorClient()


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


def convert_dates(date1_pos, date2_pos):
    # Extract date from input text
    detected_date_text = textdetect(date1_pos).strip()
    detected_date_text2 = textdetect(date2_pos).strip()

    print(detected_date_text)
    print(detected_date_text2)

    # Clean up date string
    detected_date_text = detected_date_text.replace("EXP. ", "")
    detected_date_text = detected_date_text.replace(".", "-")


    detected_date_text2 = detected_date_text2.replace(".", "-")

    # Convert date string to list
    date_list = list(detected_date_text)
    date_list2 = list(detected_date_text2)

    # Replace '8' with '0' at the first and fourth positions
    if date_list[0] == '8':
        date_list[0] = '0'
    if date_list[0] == '6':
        date_list[0] = '0'


    # Replace '8' with '0' at the first and fourth positions
    if date_list2[0] == '8':
        date_list2[0] = '0'
    if date_list2[0] == '6':
        date_list2[0] = '0'


    # Convert list back to string
    detected_date_text = ''.join(date_list)
    detected_date_text2 = ''.join(date_list2)

    print(detected_date_text)
    print(detected_date_text2)
    # Convert date string to a datetime object
    detected_date = datetime.strptime(detected_date_text, "%m-%d-%Y").date()
    detected_date_text2 = datetime.strptime(detected_date_text2, '%m-%d-%y').date()

    return detected_date, detected_date_text2

def simple_inspection(first_inspect_item_location, second_inspect_item_location):
    click_mouse(positions['Inspect_button_pos'])
    click_mouse(first_inspect_item_location)
    click_mouse(second_inspect_item_location)

    time.sleep(1.5)
    click_mouse(positions['Interrogate_pos'])
    

def set_approve():
    print("Passport Approved")
    click_mouse(positions['Stamp_tray_pos'])
    time.sleep(0.3)
    click_mouse(positions['Approval_stamp_pos'])
    drag_and_drop(positions['Approved_passport_pos'], positions['Document_drop_pos'])

def set_reject():
    print("Passport Rejected")
    click_mouse(positions['Stamp_tray_pos'])
    drag_and_drop(positions['Passport_slot_pos'], positions['Rejected_passport_pos'])
    time.sleep(0.3)
    click_mouse(positions['Rejected_stamp_pos'])
    drag_and_drop(positions['Rejected_passport_pos'], positions['Document_drop_pos'])

def text_within(input_text, input_text2):
    input_text = input_text.strip()
    input_text2 = input_text2.strip()

    input_text = input_text.lower()
    input_text2 = input_text2.lower()

    if input_text in input_text2 and input_text != " ":
        return True
    else:
        return False


def compare_colors(color1, color2):
    if color1 == color2:
        return True
    else:
        return False


def compare_pos_color(pos, input_color):
    Detected_Color = get_image_color(pos)
    
    if Detected_Color == input_color:
        return True
    else:
        return False


def not_compare_pos_color(pos, input_color):
    Detected_Color = get_image_color(pos)
    if Detected_Color == input_color:
        return False
    else:
        return True


def double_compare_pos_color(pos, input_color, input_color2):
    Detected_Color = get_image_color(pos)
    if Detected_Color == input_color or Detected_Color == input_color2:
        return True
    else:
        return False


def triple_not_compare_pos_color(pos, input_color, input_color2, input_color3):
    Detected_Color = get_image_color(pos)
    
    if Detected_Color == input_color or Detected_Color == input_color2 or Detected_Color == input_color3:
        return False
    else:
        return True


def compare_pos_text(text1_pos, text2_pos):
    text = textdetect(text1_pos)
    text2 = textdetect(text2_pos)

    text = text.strip()
    text2 = text2.strip()
    
    print(text)
    print(text2)
    if text == text2:
        return True
    else:
        return False
    
def levenshtein_ratio(string1, string2):
    distance = Levenshtein.distance(string1, string2)
    max_length = max(len(string1), len(string2))
    ratio = (max_length - distance) / max_length
    return ratio

def test_compare_pos_text(text1_pos, text2_pos):
    text = textdetect(text1_pos)
    text2 = textdetect(text2_pos)

    text = text.strip()
    text2 = text2.strip()

    text = text.replace("-", "")
    text2 = text2.replace("-", "")

    print(text)
    print(text2)

    j = levenshtein_ratio(text, text2)
    print("Levenshtein Ratio:", j)

    if ratio(text, text2) == 0.9:
        text2_pos = word_search(text, text2_pos)
    elif text == text2:
        return True
    else:
        return False


def compare_within_pos__text(text1_pos, text2_pos):
    text = textdetect(text1_pos)
    text2 = textdetect(text2_pos)

    text = text.strip()
    text2 = text2.strip()

    print(text)
    print(text2)

    result = text_within(text, text2)
    return result

def compare_names(text1_pos, text2_pos):
    text1 = textdetect(text1_pos)
    text2 = textdetect(text2_pos)

    text1 = text1.lower()
    text2 = text2.lower()

    text1 = text1.replace(".", "")
    text1 = text1.replace(",", "")

    text1 = text1.split()
    text1[0], text1[1] = text1[1], text1[0]

    modified_text1 = ' '.join(text1)  # Rejoining the words with a space in between

    print(modified_text1)
    print(text2)

    if modified_text1 == text2:
        return True
    else:
        return False


def on_date_check(detected_date_text, detected_date_text2):
    detected_date_text, detected_date_text2 = convert_dates(detected_date_text, detected_date_text2)
    if detected_date_text == detected_date_text2:
        return True
    else:
        return False


def up_to_date_check(detected_date_text, detected_date_text2):
    detected_date_text, detected_date_text2 = convert_dates(detected_date_text, detected_date_text2)
    if detected_date_text >= detected_date_text2:
        return True
    else:
        return False


def reset_person():
    Logic.PersonPresent = False
    Logic.PassportPresent = False
    Logic.StampingTime = False
    Logic.NoPassport = False
    Logic.NextPerson = False
    Logic.CorrectDate = False
    Logic.CorrectCity = False
    Logic.PersonGenderMatch = False
    Logic.PhotoPersonMatch = False
    Logic.TicketPresent = False
    Logic.ValidTicket = False
    Logic.DocumentStatus = False
    Logic.NoTicket = False
    Logic.TextBoxPresent = False
    Logic.Arstotzkan = False

    Logic.NoIdCard = False

    Logic.IdCardPresent = False
    Logic.ValidEntryPermit = False
    Logic.ValidIdCardName = False
    Logic.ValidIdCardDistrict = False
    Logic.ValidIdCardPhoto = False
    Logic.NoEntryPermit = False
    Logic.EntryPermitPresent = False
    Logic.ValidEntryPermitID = False
    Logic.ValidEntryPermitDate = False
    Logic.ValidEntryPermitDuration = False
    Logic.ValidEntryPermitName = False
    Logic.ValidEntryPermitPurpose = False
    Logic.Foreigner = False

    Logic.Approved = False
    Logic.Rejected = False
    Logic.ValidIdCard = False


def test_find_matching_key(text1_pos, text2_pos, data):
    first_string = textdetect(text1_pos)
    second_string = textdetect(text2_pos)
    
    # Convert strings to lowercase for case-insensitive comparison
    first_string_lower = first_string.lower()
    second_string_lower = second_string.lower().replace("0", "O")
    
    print("Entity Permit Text:", first_string_lower)
    print("Transcript Text:", second_string_lower)

    # Iterate through the data
    for key, values in data:
        # Check if the key matches the first string (case-insensitive)
        if first_string_lower in key.lower():
            print("Key match found:", key.lower())
            # Iterate through the values associated with the key
            for value in values:
                # Check if the value is in the second string
                if value.lower() in second_string_lower:
                    print("Value in Data:", value)
                    return True  # Exit the function once a match is found

    print("Value not in Data")
    return False

def lack_of_document(document_type):
    textbox_area = ()
    drag_and_drop(positions['Rule_book_pos'], positions['Rule_book_slot_pos'])
    click_mouse(positions['Rule_book_basics_pos'])

    if document_type == "Passport":
        
        simple_inspection(positions['Passport_rule_pos'], positions['Passport_pos'])

        click_mouse(positions['Bookmark_pos'])
        drag_and_drop(positions['Rule_book_slot_pos'], positions['Rule_book_pos'])

        while textbox_area != TEXTBOX_COLOR:
            textbox_area = get_image_color(positions['Reply_text_box_pos'])

        else:
            time.sleep(2)
            document_status = triple_not_compare_pos_color(positions['Document_area_pos'], DOCUMENT_AREA_COLOR, TICKET_COLOR, TICKET_COLOR2)
            print(document_status)
            return document_status

    elif document_type == "Ticket":
        simple_inspection(positions['Ticket_rule_pos'], positions['Secondary_document_pos'])

        click_mouse(positions['Bookmark_pos'])
        drag_and_drop(positions['Rule_book_slot_pos'], positions['Rule_book_pos'])

        while textbox_area != TEXTBOX_COLOR:
            textbox_area = get_image_color(positions['Reply_text_box_pos'])
        else:
            time.sleep(2)
            document_status = double_compare_pos_color(positions['Document_area_pos'], TICKET_COLOR, TICKET_COLOR2)
            return document_status
        
    elif document_type == "IdCard":
        simple_inspection(positions['IdCard_rule_pos'], positions['Secondary_document_pos'])

        click_mouse(positions['Bookmark_pos'])
        drag_and_drop(positions['Rule_book_slot_pos'], positions['Rule_book_pos'])

        while textbox_area != TEXTBOX_COLOR:
            textbox_area = get_image_color(positions['Reply_text_box_pos'])
        else:
            time.sleep(2)
            document_status = compare_pos_color(positions['Document_area_pos'], IDCARD_COLOR)
            return document_status
    
    elif document_type == "Entry Permit":
        simple_inspection(positions['Entry_permit_rule_pos'], positions['Secondary_document_pos'])

        click_mouse(positions['Bookmark_pos'])
        drag_and_drop(positions['Rule_book_slot_pos'], positions['Rule_book_pos'])

        while textbox_area != TEXTBOX_COLOR:
            textbox_area = get_image_color(positions['Reply_text_box_pos'])
        else:
            time.sleep(2)
            document_status = compare_pos_color(positions['Document_area_pos'], ENTRY_PERMIT_COLOR)
            return document_status

def inspection(first_inspect_item_location, second_inspect_item_location, inspect_position):
    click_mouse(positions['Inspect_button_pos'])
    click_mouse(first_inspect_item_location)
    click_mouse(second_inspect_item_location)

    time.sleep(2)
    text = textdetect(inspect_position)
    text = text.strip()

    print(text)
    click_mouse(positions['Inspect_button_pos'])
    if Matching in text:
        text = "MATCHING"
        print(text)

    if ratio(text, Matching) >= 0.75:
        return True
    else:
        return False


def set_country_positions(input_color):
    if input_color in country_dict:
        country_data = country_dict[input_color]

        country_dict['Name'] = country_data["Name"]
        country_dict['Photo_pos'] = country_data["Photo_pos"]
        country_dict['Gender_pos'] = country_data['Gender_pos']
        country_dict['Country_pos'] = country_data['Country_pos']
        country_dict['City_pos']= country_data['City_pos']
        country_dict['Date_pos'] = country_data['Date_pos']
        country_dict['Person_gender_inspect_pos'] = country_data['Person_gender_inspect_pos']
        country_dict['Photo_person_inspect_pos'] = country_data['Photo_person_inspect_pos']
        country_dict['Passport_name_pos'] = country_data['Passport_name_pos']

        if country_data["Name"] != "Arstotzka":
            country_dict['Passport_id_pos'] = country_data['Passport_id_pos']
        else:
            country_data['Passport_id_pos'] = None


        print(country_data["Name"] + "!")
        return country_data  # Return the country_data


def process_passport(passport_status):

    if passport_status == "Approved":
        set_approve()
        reset_person()

        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Accepted_person_leaving_pos'], PERSON_COLOR)

    if passport_status == "Approved 2Doc":

        set_approve()
        reset_person()
        drag_and_drop(positions['Secondary_document_slot_pos'], positions['Document_drop_pos'])

        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Accepted_person_leaving_pos'], PERSON_COLOR)

    if passport_status == "Approved 3Doc":

        set_approve()
        reset_person()
        drag_and_drop(positions['Secondary_document_slot_pos'], positions['Document_drop_pos'])

        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Accepted_person_leaving_pos'], PERSON_COLOR)

    if passport_status == "Rejected":

        set_reject()
        reset_person()

        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Rejected_person_leaving_pos'], PERSON_COLOR)

    if passport_status == "Rejected 2Doc":

        set_reject()
        reset_person()

        drag_and_drop(positions['Secondary_document_slot_pos'], positions['Document_drop_pos'])
        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Rejected_person_leaving_pos'], PERSON_COLOR)

    if passport_status == "No Passport":
        drag_and_drop(positions['Secondary_document_slot_pos'], positions['Document_drop_pos'])
        reset_person()

        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Rejected_person_leaving_pos'], PERSON_COLOR)

    if passport_status == "No Secondary":

        set_reject()
        reset_person()

        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Rejected_person_leaving_pos'], PERSON_COLOR)

    if passport_status == "No Docs":

        reset_person()

        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Rejected_person_leaving_pos'], PERSON_COLOR)

    if passport_status == "Invalid Secondary":

        set_reject()
        reset_person()
        drag_and_drop(positions['Secondary_document_slot_pos'], positions['Document_drop_pos'])
        
        while not Logic.NextPerson:
            Logic.NextPerson = compare_pos_color(positions['Rejected_person_leaving_pos'], PERSON_COLOR)


