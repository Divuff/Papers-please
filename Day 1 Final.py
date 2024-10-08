from BackEndUpdate import *
from Colors import ARSTOTZKA_COLOR, TEXTBOX_COLOR, DAY_COLOR, DOCUMENT_AREA_COLOR, WALL_COLOR, TICKET_COLOR2, \
    TICKET_COLOR

from Pos import positions
import time
import Logic

# Main program
click_mouse(positions['Lever_pos'])
click_mouse(positions['Speaker_pos'])
time.sleep(1)
Person_Leaving_Area = ()
country = ()

while get_image_color(positions['Day_test_pos']) == DAY_COLOR:

    # Check for Person Leaving/Entering
    if Logic.NextPerson:
        Logic.NextPerson = False
        click_mouse(positions['Speaker_pos'])
        print("Ready for Next Person")

    # Check if person is present
    Logic.PersonPresent = not_compare_pos_color(positions['Person_pos'], WALL_COLOR)
    if Logic.PersonPresent and not Logic.StampingTime:
        time.sleep(1)
        print("Person Detected")

    Logic.TextBoxPresent = compare_pos_color(positions['Primary_text_box_pos'], TEXTBOX_COLOR)
    if Logic.TextBoxPresent and Logic.PersonPresent:
        time.sleep(1.5)
        Logic.PassportPresent = triple_not_compare_pos_color(positions['Document_area_pos'], DOCUMENT_AREA_COLOR,
                                                             TICKET_COLOR,
                                                             TICKET_COLOR2)
        if Logic.PassportPresent:
            drag_and_drop(positions['Passport_pos'], positions['Passport_slot_pos'])
            country = get_image_color(positions['Passport_border_pos'])
            print("Passport Detected")
        else:
            Logic.NoPassport = True
            print("No Passport!")

        if country != ARSTOTZKA_COLOR:
            Logic.Arstotzkan = False
            Logic.Foreigner = True
        else:
            Logic.Foreigner = False
            Logic.Arstotzkan = True
            print("Arstotzkan Detected")

    if Logic.NoPassport:
        Logic.DocumentStatus = lack_of_document("Passport")
        click_mouse(positions['Bookmark_pos'])

        if Logic.DocumentStatus:
            Logic.NoPassport = False
            Logic.PassportPresent = True
            Logic.StampingTime = False
        else:
            Logic.PassportPresent = False
            Logic.StampingTime = True

    if Logic.PersonPresent and Logic.PassportPresent:
        Logic.StampingTime = True

    # APPROVAL STAMP
    if Logic.StampingTime:
        if Logic.Arstotzkan:
            process_passport("Approved")

        # REJECTED STAMP
        elif Logic.Foreigner:
            process_passport("Rejected")

        # NO PASSPORT
        if Logic.NoPassport:
            process_passport("No Passport")
