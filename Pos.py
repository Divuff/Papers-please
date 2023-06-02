# Pos.py
from Colors import ARSTOTZKA_COLOR, ANTEGRIA_COLOR, OBRISTAN_COLOR, IMPOR_COLOR, KOLECHIA_COLOR, UNITEDFED_COLOR, \
    REPUBLIA_COLOR

positions = {
    'Primary_text_box_pos': (140, 535),
    'Passport_side_pos': (175, 1085),
    'Clock_pos': (148, 1320, 271, 1356),

    'Passport_pos': (475, 1085),
    'Document_drop_pos': (480, 700),
    'Person_pos': (490, 850),
    'Secondary_document_pos': (500, 1065),
    'Interrogate_pos': (500, 1230),
    'Document_area_pos': (500, 1080),

    'Rule_book_pos': (640, 1250),
    'Rejected_person_leaving_pos': (700, 430),
    'Speaker_pos': (830, 370),
    'Reply_text_box_pos': (840, 600),
    'Lever_pos': (850, 550),
    'Bookmark_pos': (870, 750),
    'Accepted_person_leaving_pos': (960, 430),

    'Passport_rule_pos': (1000, 850),
    'Ticket_rule_pos': (1035, 1055),
    'IdCard_rule_pos': (1035, 1055),
    'Secondary_document_slot_pos': (1260, 625),

    'Rule_book_slot_pos': (1300, 1050),
    'Issuing_cities_pos': (1400, 1120),
    'Day_test_pos': (1444, 180),
    'Rule_book_basics_pos': (1500, 910),

    'Regional_map_pos': (1510, 970),
    'Rejected_stamp_pos': (1600, 695),
    'Rejected_passport_pos': (1600, 950),

    'Passport_border_pos': (1845, 950),

    'Passport_slot_pos': (2100, 950),
    'Approval_stamp_pos': (2100, 730),
    'Approved_passport_pos': (2100, 950),

    'Inspect_button_pos': (2350, 1320),
    'Stamp_tray_pos': (2400, 730),

    'Issuing_city_pos': (1370, 1080, 1620, 1200),

    'Ticket_date_pos': (1330, 645, 1505, 690),

    'Idcard_district_pos': (1020, 525, 1305, 550),
    'Idcard_name_pos': (1200, 562, 1362, 617),
    'Idcard_photo_pos': (1100, 675),

    'Idcard_passport_photo_pos': (1408, 846, 1615, 917),

    'District_pos': (910, 900, 1140, 1200),

    'Entry_permit_name_pos': (1016, 584, 1491, 615),
    'Entry_permit_id_pos': (1135, 714, 1357, 748),
    'Entry_permit_purpose_pos': (1227, 783, 1407, 807),
    'Entry_permit_duration_pos': (1237, 841, 1394, 869),
    'Entry_permit_date_pos': (1160, 900, 1491, 930),
    'Entry_permit_rule_pos': (1020, 1155),
    
    'Transcript_slot_pos': (2020, 1200),
    'Transcript_text_pos': (1760, 850, 2283, 1182)
}

NAME = ""

country_dict = {
    ARSTOTZKA_COLOR: {
        'Name': 'Arstotzka',
        'Photo_pos': (1920, 1120),
        'Gender_pos': (2128, 1060),
        'Country_pos': (1650, 1080),
        'Date_pos': (2035, 1111, 2288, 1140),
        'City_pos': (2108, 1078, 2321, 1106),

        'Person_gender_inspect_pos': (1260, 865, 1490, 955),
        'Photo_person_inspect_pos': (1145, 880, 1360, 970),
        
        'Passport_name_pos': ()
    },
    ANTEGRIA_COLOR: {
        'Name': 'Antegria',
        'Photo_pos': (2255, 1083),
        'Gender_pos': (1947, 1073),
        'Country_pos': (1033, 952),

        'Date_pos': (1935, 1137, 2115, 1162),
        'City_pos': (1935, 1097, 2170, 1127),
        'Person_gender_inspect_pos': (1180, 870, 1400, 955),
        'Photo_person_inspect_pos': (1300, 865, 1520, 985),
        
        'Passport_name_pos': (1870, 1179, 2062, 1205),
        'Passport_id_pos': (2103, 1214, 2330, 1248)
    },
    OBRISTAN_COLOR: {
        'Name': 'Obristan',
        'Photo_pos': (2250, 1150),
        'Gender_pos': (1958, 1111),
        'Country_pos': (1150, 780),

        'Date_pos': (1940, 1163, 2120, 1190),
        'City_pos': (1945, 1130, 2130, 1165),
        'Person_gender_inspect_pos': (1185, 890, 1400, 970),
        'Photo_person_inspect_pos': (1300, 900, 1510, 1002),
        
        'Passport_name_pos': (1871, 1015, 2200, 1040),
        'Passport_id_pos': (1878, 1215, 2097, 1239)
    },
    IMPOR_COLOR: {
        'Name': 'Impor',
        'Photo_pos': (1920, 1150),
        'Gender_pos': (2128, 1054),
        'Country_pos': (1190, 1270),

        'Date_pos': (2115, 1108, 2325, 1136),
        'City_pos': (2115, 1075, 2325, 1105),
        'Person_gender_inspect_pos': (1260, 860, 1495, 950),
        'Photo_person_inspect_pos': (1150, 880, 1370, 970),
        
        'Passport_name_pos': (1871, 967, 2200, 998),
        'Passport_id_pos': (2091, 1207, 2316, 1231)
    },
    KOLECHIA_COLOR: {
        'Name': 'Kolechia',
        'Photo_pos': (1920, 1150),
        'Gender_pos': (2128, 1095),
        'Country_pos': (1450, 810),

        'Date_pos': (2115, 1145, 2300, 1178),
        'City_pos': (2115, 1115, 2330, 1143),
        'Person_gender_inspect_pos': (1260, 875, 1495, 969),
        'Photo_person_inspect_pos': (1150, 910, 1370, 992),
        
        'Passport_name_pos': (1870, 1016, 2153, 1042),
        'Passport_id_pos': (2104, 1213, 2326, 1241)
    },
    UNITEDFED_COLOR: {
        'Name': 'UnitedFed',
        'Photo_pos': (1920, 1150),
        'Gender_pos': (2128, 1095),
        'Country_pos': (900, 1220),

        'Date_pos': (2115, 1144, 2300, 1170),
        'City_pos': (2115, 1111, 2315, 1143),
        'Person_gender_inspect_pos': (1260, 875, 1495, 969),
        'Photo_person_inspect_pos': (1150, 900, 1400, 1000),
        
        'Passport_name_pos': (1871, 1015, 2200, 1040),
        'Passport_id_pos': (2108, 1208, 2335, 1247)
    },
    REPUBLIA_COLOR: {
        'Name': 'Republia',
        'Photo_pos': (2250, 1110),
        'Gender_pos': (1962, 1055),
        'Country_pos': (1100, 1120),

        'Date_pos': (1945, 1110, 2125, 1140),
        'City_pos': (1945, 1080, 2155, 1105),
        'Person_gender_inspect_pos': (1185, 860, 1410, 950),
        'Photo_person_inspect_pos': (1300, 880, 1520, 970),
        
        'Passport_name_pos': (1871, 972, 2108, 997),
        'Passport_id_pos': (2098, 1207, 2317, 1232)
    }
}
