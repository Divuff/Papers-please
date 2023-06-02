from EOF.BackEnd import *
from Colors import ARSTOTZKA_COLOR, PERSON_COLOR, DAY_COLOR, WALL_COLOR
from Pos import LEVER_POS, SPEAKER_POS, DAY_TEST_POS, PERSON_POS, Primary_text_box_pos, \
    PASSPORT_BORDER_POS, BOOKMARK_POS, \
    TICKET_DATE_POS, RULE_BOOK_POS, RULE_BOOK_SLOT_POS, REGIONAL_MAP_POS, ISSUING_CITY_POS, \
    SECONDARY_DOCUMENT_SLOT_POS, ACCEPTED_PERSON_LEAVING_POS, \
    REJECTED_PERSON_LEAVING_POS

Date = "11-25-1982"

# Functions


# DaySTART
click_mouse(LEVER_POS)
click_mouse(SPEAKER_POS)

name = ()
matching_country = ()
person_leaving_area = ()

while get_image_color(DAY_TEST_POS) == DAY_COLOR:
    lady_worker()

    # Person Leaving Booth Check
    if person_leaving_area == PERSON_COLOR:
        Logic.NextPerson = True
        person_leaving_area = ()
        click_mouse(SPEAKER_POS)
        print("Ready for Next Person")
    else:
        Logic.NextPerson = False

    # Check if person is present
    person_area = get_image_color(PERSON_POS)
    if person_area != WALL_COLOR:
        if not Logic.PersonPresent:
            Logic.PersonPresent = True
            print("Person Detected")
    else:
        Logic.PersonPresent = False

    # Check if text box is present
    Logic.TextBoxPresent = textbox_check(Primary_text_box_pos)
    if Logic.TextBoxPresent and Logic.PersonPresent:

        Logic.PassportPresent = passport_check()
        country = get_image_color(PASSPORT_BORDER_POS)

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
        click_mouse(BOOKMARK_POS)

        if Logic.DocumentStatus:
            Logic.NoPassport = False
            Logic.PassportPresent = True
            Logic.StampingTime = False
        else:
            Logic.PassportPresent = False
            Logic.StampingTime = True

    elif Logic.NoTicket:
        Logic.DocumentStatus = lack_of_document("Ticket")
        click_mouse(BOOKMARK_POS)

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
        country = get_image_color(PASSPORT_BORDER_POS)
        set_country_positions(country)

    if Logic.StampingTime:

        if Logic.TicketPresent:
            Logic.ValidTicket = on_date_check(TICKET_DATE_POS, Date)

        if Logic.ValidTicket or Logic.Arstotzkan:
            # MOVE RULE
            drag_and_drop(RULE_BOOK_POS, RULE_BOOK_SLOT_POS)

            # CHECK CITY
            click_mouse(REGIONAL_MAP_POS)
            click_mouse(Logic.COUNTRY_POS)

            print("Valid Ticket")

            print(Logic.CITY_POS)  # Should output a sequence with 2 or 4 elements
            print(ISSUING_CITY_POS)  # Should output a sequence with 2 or 4 elements

            Logic.CorrectCity = compare_city(Logic.CITY_POS, ISSUING_CITY_POS)
            click_mouse(BOOKMARK_POS)
            drag_and_drop(RULE_BOOK_SLOT_POS, RULE_BOOK_POS)

        # Validate Issuing City
        if Logic.CorrectCity:
            print("Valid issuing city!")
            Logic.CorrectDate = up_to_date_check(Logic.DATE_POS, Date)
        else:
            print("Invalid issuing city!")

        if Logic.CorrectDate:
            inspection(Logic.GENDER_POS, PERSON_POS)
            Logic.PersonGenderMatch = inspect_detect(Logic.PERSON_GENDER_INSPECT_POS)
            print("Valid Date!")
        else:
            print("Passport Out Of Date!")

        if Logic.PersonGenderMatch:
            inspection(Logic.PHOTO_POS, PERSON_POS)
            Logic.PhotoPersonMatch = inspect_detect(Logic.PHOTO_PERSON_INSPECT_POS)
            print("Valid Gender!")
        else:
            print("InValid Gender!")

        if Logic.PhotoPersonMatch:
            print("VALID PASSPORT!")
            process_passport("Approved")
            reset_person()

            return_documents(SECONDARY_DOCUMENT_SLOT_POS)

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(ACCEPTED_PERSON_LEAVING_POS)

        elif Logic.NoPassport and Logic.NoTicket:
            print("NO DOCUMENTS")
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POS)

        elif Logic.NoPassport:
            print("NO PASSPORT")

            reset_person()
            return_documents(SECONDARY_DOCUMENT_SLOT_POS)

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POS)

        elif Logic.NoTicket:
            print("NO TICKET")

            process_passport("Rejected")
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POS)

        elif not Logic.ValidTicket:
            print("INVALID TICKET")
            process_passport("Rejected")
            return_documents(SECONDARY_DOCUMENT_SLOT_POS)
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POS)

        else:
            print("INVALID PASSPORT")
            process_passport("Rejected")
            return_documents(SECONDARY_DOCUMENT_SLOT_POS)
            reset_person()

            while person_leaving_area != PERSON_COLOR:
                person_leaving_area = get_image_color(REJECTED_PERSON_LEAVING_POS)
