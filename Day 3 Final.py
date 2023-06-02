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
            print("Passport Detected")
            drag_and_drop(positions['Passport_pos'], positions['Passport_slot_pos'])
            country = get_image_color(positions['Passport_border_pos'])
            country_data = set_country_positions(country)
        else:
            Logic.NoPassport = True
            print("No Passport!")

        if country != ARSTOTZKA_COLOR:
            Logic.Arstotzkan = False
            Logic.Foreigner = True
            Logic.TicketPresent = double_compare_pos_color(positions['Document_area_pos'], TICKET_COLOR, TICKET_COLOR2)
        else:
            Logic.Foreigner = False
            Logic.Arstotzkan = True
            print("Arstotzkan Detected")

        if Logic.TicketPresent:
            print("Ticket Present")
            drag_and_drop(positions['Secondary_document_pos'], positions['Secondary_document_slot_pos'])

            Logic.NoTicket = False
        elif Logic.Arstotzkan:
            Logic.NoTicket = False
        else:
            print("No ticket")
            Logic.NoTicket = True
   
        
    if Logic.NoPassport:
        Logic.DocumentStatus = lack_of_document("Passport")


        if Logic.DocumentStatus:
            drag_and_drop(positions['Passport_pos'], positions['Passport_slot_pos'])
            country = get_image_color(positions['Passport_border_pos'])
            country_data = set_country_positions(country)
            
            Logic.NoPassport = False
            Logic.PassportPresent = True
            Logic.StampingTime = False
            
            print(Logic.StampingTime)
        else:
            Logic.PassportPresent = False
            Logic.StampingTime = True
            
            print(Logic.StampingTime)
        
    elif Logic.NoTicket:
        Logic.DocumentStatus = lack_of_document("Ticket")

        if Logic.DocumentStatus:
            Logic.NoTicket = False
            Logic.TicketPresent = True
            Logic.StampingTime = False
            drag_and_drop(positions['Secondary_document_pos'], positions['Secondary_document_slot_pos'])
        else:
            Logic.TicketPresent = False
            Logic.StampingTime = True

     
    if Logic.PersonPresent and Logic.PassportPresent:
        Logic.StampingTime = True

        # APPROVAL STAMP
    
    if Logic.StampingTime:
        
        if Logic.TicketPresent:
            Logic.ValidTicket = on_date_check(positions['Ticket_date_pos'], positions['Clock_pos'])
                
        if Logic.ValidTicket or Logic.Arstotzkan:
            drag_and_drop(positions['Rule_book_pos'], positions['Rule_book_slot_pos'])
            click_mouse(positions['Regional_map_pos'])
            click_mouse(country_data['Country_pos'])

            Logic.CorrectCity = compare_within_pos__text(country_data['City_pos'], positions['Issuing_city_pos'])

            click_mouse(positions['Bookmark_pos'])
            drag_and_drop(positions['Rule_book_slot_pos'], positions['Rule_book_pos'])

            if Logic.CorrectCity:
                print("Valid issuing city!")
                Logic.CorrectDate = up_to_date_check(country_data['Date_pos'], positions['Clock_pos'])

                if Logic.CorrectDate:
                    print("Valid Date!")

            if Logic.CorrectCity and Logic.CorrectDate:
                Logic.PersonGenderMatch = inspection(country_data['Gender_pos'], positions['Person_pos'], country_data['Person_gender_inspect_pos'])

                if Logic.PersonGenderMatch:
                    print("Valid Gender!")

            if Logic.PersonGenderMatch:
                Logic.PhotoPersonMatch = inspection(country_data['Photo_pos'], positions['Person_pos'], country_data['Photo_person_inspect_pos'])

                if Logic.PhotoPersonMatch:
                    print("Valid Photo!")

            if Logic.PhotoPersonMatch:
                process_passport("Approved 2Doc")

            elif Logic.Arstotzkan and Logic.PhotoPersonMatch:
                process_passport("Approved")

            # NO DOCUMENTS
            elif Logic.NoTicket and Logic.NoPassport:
                print("No Documents")
                process_passport("No Docs")

            # NO PASSPORT
            elif Logic.NoPassport:
                print("No passport")
                process_passport("No Passport")

            # NO TICKET
            elif Logic.NoTicket:
                print("No Ticket")
                process_passport("No Secondary")

            # Invalid Ticket
            elif not Logic.ValidTicket:
                print("Invalid Ticket")
                process_passport("Invalid Secondary")

            # REJECTED STAMP
            else:
                print("Rejected")
                process_passport("Rejected 2Doc")