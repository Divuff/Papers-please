import Logic
from BackEnd import get_image_color, click_mouse, lady_worker, textbox_check, passport_check, ticket_check, \
    lack_of_document, on_date_check, drag_and_drop, \
    up_to_date_check, compare_city, inspection, inspect_detect, reset_person, return_documents, \
    process_passport, set_country_positions
from Colors import ARSTOTZKA_COLOR, PERSON_COLOR, DAY_COLOR, WALL_COLOR
from Positions import LEVER_POSITION, SPEAKER_POSITION, DAY_TEST_POSITION, PERSON_POSITION, PRIMARY_TEXT_BOX_POSITION, \
    PASSPORT_BORDER_POSITION, BOOKMARK_POSITION, \
    TICKET_DATE_POSITION, RULE_BOOK_POSITION, RULE_BOOK_SLOT_POSITION, REGIONAL_MAP_POSITION, ISSUING_CITY_POS, \
    SECONDARY_DOCUMENT_SLOT_POSITION, ACCEPTED_PERSON_LEAVING_POSITION, \
    REJECTED_PERSON_LEAVING_POSITION

Date = "11-25-1982"

# Functions


# DaySTART
click_mouse(LEVER_POSITION)
click_mouse(SPEAKER_POSITION)

name = ()
matching_country = ()
person_leaving_area = ()

while get_image_color(DAY_TEST_POSITION) == DAY_COLOR:
    lady_worker()

    # Person Leaving Booth Check
    if person_leaving_area == PERSON_COLOR:
        Logic.NextPerson = True
        person_leaving_area = ()
        click_mouse(SPEAKER_POSITION)
        print("Ready for Next Person")
    else:
        Logic.NextPerson = False

    # Check if person is present
    person_area = get_image_color(PERSON_POSITION)
    if person_area != WALL_COLOR:
        if not Logic.PersonPresent:
            Logic.PersonPresent = True
            print("Person Detected")
    else:
        Logic.PersonPresent = False

    # Check if text box is present
    Logic.TextBoxPresent = textbox_check(PRIMARY_TEXT_BOX_POSITION)
    if Logic.TextBoxPresent and Logic.PersonPresent:

        Logic.PassportPresent = passport_check()
        country = get_image_color(PASSPORT_BORDER_POSITION)

        if country != ARSTOTZKA_COLOR:
            Logic.Arstotzkan = False
            Logic.Foreigner = True
            Logic.TicketPresent = ticket_check()
        else:
            Logic.Foreigner = False
            Logic.Arstotzkan = True
            print("Arstotzkan Detected")

        if Logic.PassportPresent:
            print("Passport Detected")
        else:
            Logic.NoPassport = True
            print("No Passport!")

        if Logic.TicketPresent or Logic.Arstotzkan:
            print("Ticket Present")
            Logic.NoTicket = False
        else:
            print("No ticket")
            Logic.NoTicket = True

    if Logic.NoPassport:
        Logic.DocumentStatus = lack_of_document("Passport")
        click_mouse(BOOKMARK_POSITION)

        if Logic.DocumentStatus:
            Logic.NoPassport = False
            Logic.PassportPresent = True
            Logic.StampingTime = False
        else:
            Logic.PassportPresent = False
            Logic.StampingTime = True

    elif Logic.NoTicket:
        Logic.DocumentStatus = lack_of_document("Ticket")
        click_mouse(BOOKMARK_POSITION)

        if Logic.DocumentStatus:
            Logic.NoTicket = False
            Logic.TicketPresent = True
            Logic.StampingTime = False

        else:
            Logic.TicketPresent = False
            Logic.StampingTime = True

    if Logic.PersonPresent and Logic.PassportPresent:
        Logic.StampingTime = True

        # Example usage
        country = get_image_color(PASSPORT_BORDER_POSITION)
        set_country_positions(country)

    if Logic.StampingTime:

        if Logic.TicketPresent:
            Logic.ValidTicket = on_date_check(TICKET_DATE_POSITION, Date)

        if Logic.ValidTicket or Logic.Arstotzkan:
            # MOVE RULE
            drag_and_drop(RULE_BOOK_POSITION, RULE_BOOK_SLOT_POSITION)

            # CHECK CITY
            click_mouse(REGIONAL_MAP_POSITION)
            click_mouse(Logic.COUNTRY_POSITION)

            print("Valid Ticket")

            print(Logic.CITY_POSITION)  # Should output a sequence with 2 or 4 elements
            print(ISSUING_CITY_POS)  # Should output a sequence with 2 or 4 elements

            Logic.CorrectCity = compare_city(Logic.CITY_POSITION, ISSUING_CITY_POS)
            click_mouse(BOOKMARK_POSITION)
            drag_and_drop(RULE_BOOK_SLOT_POSITION, RULE_BOOK_POSITION)

        # Validate Issuing City
        if Logic.CorrectCity:
            print("Valid issuing city!")
            Logic.CorrectDate = up_to_date_check(Logic.DATE_POSITION, Date)
        else:
            print("Invalid issuing city!")

        if Logic.CorrectDate:
            inspection(Logic.GENDER_POSITION, PERSON_POSITION)
            Logic.PersonGenderMatch = inspect_detect(Logic.PERSON_GENDER_INSPECT_POSITION)
            print("Valid Date!")
        else:
            print("Passport Out Of Date!")

        if Logic.PersonGenderMatch:
            inspection(Logic.PHOTO_POSITION, PERSON_POSITION)
            Logic.PhotoPersonMatch = inspect_detect(Logic.PHOTO_PERSON_INSPECT_POSITION)
            print("Valid Gender!")
        else:
            print("InValid Gender!")

        if Logic.PhotoPersonMatch:
            print("VALID PASSPORT!")
            process_passport("Approved")
            reset_person()

            return_documents(SECONDARY_DOCUMENT_SLOT_POSITION)

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(ACCEPTED_PERSON_LEAVING_POSITION)

        elif Logic.NoPassport and Logic.NoTicket:
            print("NO DOCUMENTS")
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)

        elif Logic.NoPassport:
            print("NO PASSPORT")

            reset_person()
            return_documents(SECONDARY_DOCUMENT_SLOT_POSITION)

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)

        elif Logic.NoTicket:
            print("NO TICKET")

            process_passport("Rejected")
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)

        elif not Logic.ValidTicket:
            print("INVALID TICKET")
            process_passport("Rejected")
            return_documents(SECONDARY_DOCUMENT_SLOT_POSITION)
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)

        else:
            print("INVALID PASSPORT")
            process_passport("Rejected")
            return_documents(SECONDARY_DOCUMENT_SLOT_POSITION)
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POSITION)
