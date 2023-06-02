from BackEndUpdate import *
from Colors import ARSTOTZKA_COLOR, ENTRY_PERMIT_COLOR2, TEXTBOX_COLOR, DAY_COLOR, DOCUMENT_AREA_COLOR, WALL_COLOR, TICKET_COLOR2, \
    TICKET_COLOR, ENTRY_PERMIT_COLOR

from Pos import positions
import time
from Logic import *

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
            Logic.EntryPermitPresent = double_compare_pos_color(positions['Document_area_pos'], ENTRY_PERMIT_COLOR, ENTRY_PERMIT_COLOR2)
        else:
            Logic.Foreigner = False
            Logic.Arstotzkan = True
            ValueError("Arstotzkan Detected")
            Logic.IdCardPresent = compare_pos_color(positions['Document_area_pos'], IDCARD_COLOR)

        if Logic.EntryPermitPresent and Logic.Foreigner:
            print("Entry Permit Present")
            drag_and_drop(positions['Secondary_document_pos'], positions['Secondary_document_slot_pos'])
            Logic.NoTicket = False
        elif Logic.Foreigner:
            Logic.NoEntryPermit = True
        
        if Logic.IdCardPresent and Logic.Arstotzkan:
             print("IdCard Present")
        elif Logic.Arstotzkan:
             Logic.NoIdCard = True
        
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
        
    elif Logic.NoIdCard:
        Logic.DocumentStatus = lack_of_document("IdCard")

        if Logic.DocumentStatus:
            Logic.NoIdCard = False
            Logic.IdCardPresent = True
            Logic.StampingTime = False
            drag_and_drop(positions['Secondary_document_pos'], positions['Secondary_document_slot_pos'])
        else:
            Logic.IdCardPresent = False
            Logic.StampingTime = True

    elif Logic.NoEntryPermit:
        Logic.DocumentStatus = lack_of_document("Entry Permit")

        if Logic.DocumentStatus:
            Logic.NoTicket = False
            Logic.EntryPermitPresent = True
            Logic.StampingTime = False
            drag_and_drop(positions['Secondary_document_pos'], positions['Secondary_document_slot_pos'])
        else:
            Logic.EntryPermitPresent = False
            Logic.StampingTime = True
    
    
    if Logic.PersonPresent and Logic.PassportPresent:
        Logic.StampingTime = True
    

    if Logic.StampingTime:
        
        if Logic.EntryPermitPresent and Logic.Foreigner:
                Logic.ValidEntryPermitName = compare_names(country_data['Passport_name_pos'], positions ['Entry_permit_name_pos'])
                Logic.ValidEntryPermitID = compare_pos_text(country_data['Passport_id_pos'], positions['Entry_permit_id_pos'])
                Logic.ValidEntryPermitDate = up_to_date_check(positions['Entry_permit_date_pos'], positions['Clock_pos'])
                
                drag_and_drop(positions['Interrogate_pos'], positions['Transcript_slot_pos'])

                Logic.ValidEntryPermitPurpose = find_matching_key(positions['Entry_permit_purpose_pos'], positions['Transcript_text_pos'], purpose_dict)

                Logic.ValidEntryPermitDuration = find_matching_key(positions['Entry_permit_duration_pos'], positions['Transcript_text_pos'], time_length_dict)

                drag_and_drop(positions['Transcript_slot_pos'], positions['Interrogate_pos'])

        if Logic.ValidEntryPermitName and Logic.ValidEntryPermitID and Logic.ValidEntryPermitDate and Logic.ValidEntryPermitPurpose and Logic.ValidEntryPermitDuration:

            Logic.ValidEntryPermit = True
            print("Valid Entry Permit")

        # Thank me Later :)
        #elif not Logic.ValidEntryPermitName:
            simple_inspection(country_data['Passport_name_pos'], positions ['Entry_permit_name_pos'])
        #elif not Logic.ValidEntryPermitName:
            simple_inspection(country_data['Passport_id_pos'], positions['Entry_permit_id_pos'])
        #elif not Logic.ValidEntryPermitDate:
            simple_inspection(positions['Entry_permit_date_pos'], positions['Clock_pos'])
        #elif not Logic.ValidEntryPermitPurpose: 
            simple_inspection(positions['Entry_permit_purpose_pos'], positions['Transcript_text_pos'])
        #elif Logic.ValidEntryPermitDuration:
            simple_inspection(positions['Entry_permit_duration_pos'], positions['Transcript_text_pos'])
           
                
        if Logic.ValidEntryPermit or Logic.ValidIdCard:
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
                Logic.Approved = True
                
        elif Logic.Approved:
            process_passport("Approved 2Doc")

        # NO DOCUMENTS
        elif Logic.NoEntryPermit and Logic.NoPassport:
            print("No Documents")
            process_passport("No Docs")

        # NO DOCUMENTS
        elif Logic.NoIdCard and Logic.NoPassport:
            print("No Documents")
            process_passport("No Docs")

        # NO PASSPORT
        elif Logic.NoPassport:
            print("No passport")
            process_passport("No Passport")

        # NO TICKET
        elif Logic.NoEntryPermit:
            print("No NoEntryPermit")
            process_passport("No Secondary")

        # NO TICKET
        elif Logic.NoIdCard:
                print("No IdCard")
                process_passport("No Secondary")

        # Invalid Ticket
        elif not Logic.ValidEntryPermit:
            print("Invalid Entry Permit")
            process_passport("Invalid Secondary")

        # Invalid Ticket
        elif not Logic.ValidIdCard:
            print("Invalid Idcard ")
            process_passport("Invalid Secondary")

        # REJECTED STAMP
        else:
            print("Rejected")
            process_passport("Rejected 2Doc")
