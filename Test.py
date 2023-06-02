from Logic import *

from BackEndUpdate import *

country = get_image_color(positions['Passport_border_pos'])
country_data = set_country_positions(country)


# Durtaion Code

Logic.ValidEntryPermitName = compare_names(country_data['Passport_name_pos'], positions ['Entry_permit_name_pos'])
Logic.ValidEntryPermitID = compare_pos_text(country_data['Passport_id_pos'], positions['Entry_permit_id_pos'])
Logic.ValidEntryPermitDate = up_to_date_check(positions['Entry_permit_date_pos'], positions['Clock_pos'])
                
drag_and_drop(positions['Interrogate_pos'], positions['Transcript_slot_pos'])

Logic.ValidEntryPermitPurpose = find_matching_key(positions['Entry_permit_purpose_pos'], positions['Transcript_text_pos'], purpose_dict)

Logic.ValidEntryPermitDuration = find_matching_key(positions['Entry_permit_duration_pos'], positions['Transcript_text_pos'], time_length_dict)

drag_and_drop(positions['Transcript_slot_pos'], positions['Interrogate_pos'])

print(Logic.ValidEntryPermitName)
print(Logic.ValidEntryPermitID)
print(Logic.ValidEntryPermitDate)
print(Logic.ValidEntryPermitPurpose)
print(Logic.ValidEntryPermitDuration)


if Logic.ValidEntryPermitName and Logic.ValidEntryPermitID and Logic.ValidEntryPermitDate and Logic.ValidEntryPermitPurpose and Logic.ValidEntryPermitDuration:

    Logic.ValidEntryPermit = True
    
    print("Valid Entry Permit")

