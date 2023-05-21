import Logic
from BackEndUpdate import *
from Positions import LEVER_POSITION, SPEAKER_POSITION, DAY_TEST_POSITION, PERSON_POSITION, PRIMARY_TEXT_BOX_POSITION, \
    PASSPORT_BORDER_POSITION, BOOKMARK_POSITION, \
    TICKET_DATE_POSITION, RULE_BOOK_POSITION, RULE_BOOK_SLOT_POSITION, REGIONAL_MAP_POSITION, ISSUING_CITY_POS, \
    SECONDARY_DOCUMENT_SLOT_POSITION, ACCEPTED_PERSON_LEAVING_POSITION, \
    REJECTED_PERSON_LEAVING_POSITION

from Colors import ARSTOTZKA_COLOR, PERSON_COLOR, TEXTBOX_COLOR, DAY_COLOR, DOCUMENT_AREA_COLOR, WALL_COLOR

# Main program
click_mouse(LEVER_POSITION)
click_mouse(SPEAKER_POSITION)
time.sleep(1)
Person_Leaving_Area = ()
country = ()

while get_image_color(DAY_TEST_POSITION) == DAY_COLOR:

    # Check for Person Leaving/Entering
    if Person_Leaving_Area == PERSON_COLOR:
        Logic.NextPerson = True
        person_leaving_area = ()
        click_mouse(SPEAKER_POSITION)
        print("Ready for Next Person")
    else:
        Logic.NextPerson = False

    # Check if person is present
    Logic.PersonPresent = get_image_color(PERSON_POSITION)
    if Logic.PassportPresent:
        Logic.PersonPresent = True
        print("Person Detected")
    else:
        Logic.PersonPresent = False

    # Check if text box is present
    Logic.TextBoxPresent = compare_pos_color(PRIMARY_TEXT_BOX_POSITION, TEXTBOX_COLOR)
    if Logic.TextBoxPresent and Logic.PersonPresent:

        Logic.PassportPresent = triple_not_compare_pos_color(DOCUMENT_AREA_POSITION, DOCUMENT_AREA_COLOR, TICKET_COLOR, TICKET_COLOR2)

        if Logic.PassportPresent:
            country = get_image_color(PASSPORT_BORDER_POSITION)
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

    if Logic.PersonPresent and Logic.PassportPresent:
        StampingTime = True

    # APPROVAL STAMP
    if StampingTime:
        if Logic.Arstotzkan:
            print(process_passport("Approved"))


        # REJECTED STAMP
        elif Logic.Foreigner:
            print(process_passport("Rejected"))


        # NO PASSPORT
        if Logic.NoPassport:
            print(process_passport("No_Passport"))
