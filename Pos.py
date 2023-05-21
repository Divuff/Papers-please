# Positions.py
from Colors import ARSTOTZKA_COLOR, ANTEGRIA_COLOR, OBRISTAN_COLOR, IMPOR_COLOR, KOLECHIA_COLOR, UNITEDFED_COLOR, \
    REPUBLIA_COLOR

PRIMARY_TEXT_BOX_POS = (140, 535)
PASSPORT_SIDE_POS = (175, 1085)
CLOCK_POS = (148, 1320, 271, 1356)


PASSPORT_POS = (475, 1085)
DOCUMENT_DROP_POS = (480, 700)
PERSON_POS = (490, 850)
SECONDARY_DOCUMENT_POS = (500, 1065)
INTERROGATE_POS = (500, 1230)
DOCUMENT_AREA_POS = (500, 1080)

RULE_BOOK_POS = (640, 1250)
REJECTED_PERSON_LEAVING_POS = (700, 430)
SPEAKER_POS = (830, 370)
REPLY_TEXT_BOX_POS = (840, 600)
LEVER_POS = (850, 550)
BOOKMARK_POS = (870, 750)
ACCEPTED_PERSON_LEAVING_POS = (960, 430)

PASSPORT_RULE_POS = (1000, 850)
TICKET_RULE_POS = (1035, 1055)
SECONDARY_DOCUMENT_SLOT_POS = (1260, 625)

RULE_BOOK_SLOT_POS = (1300, 1050)
ISSUING_CITIES_POS = (1400, 1120)
DAY_TEST_POS = (1444, 180)
RULE_BOOK_BASICS_POS = (1500, 910)

REGIONAL_MAP_POS = (1510, 970)
REJECTED_STAMP_POS = (1600, 695)
REJECTED_PASSPORT_POS = (1600, 950)

PASSPORT_BORDER_POS = (1845, 950)

PASSPORT_SLOT_POS = (2100, 950)
APPROVAL_STAMP_POS = (2100, 730)
APPROVED_PASSPORT_POS = (2100, 950)

INSPECT_BUTTON_POS = (2350, 1320)
STAMP_TRAY_POS = (2400, 730)

ISSUING_CITY_POS = (1370, 1080, 1620, 1200)

TICKET_DATE_POS = (1330, 645, 1505, 690)

IDCARD_DISTRICT_POS = (1020, 525, 1305, 550)
IDCARD_NAME_POS = (1200, 562, 1362, 617)
IDCARD_PHOTO_POS = (1100, 675)

IDCARD_PASSPORT_PHOTO_POS = (1408, 846, 1615, 917)

DISTRICT_POS = (910, 900, 1140, 1200)

ENTRY_PERMIT_NAME_POS = (1214, 598)
ENTRY_PERMIT_ID_POS = (1215, 731)
ENTRY_PERMIT_PURPOSE_POS = (1320, 794)
ENTRY_PERMIT_DURATION_POS = (1315, 860)
ENTRY_PERMIT_DATE_POS = (1315, 918)


DATE_POS = ()
PHOTO_POS = ()
CITY_POS = ()
GENDER_POS = ()

COUNTRY_POS = ()
PHOTO_GENDER_INSPECT_POS = ()
PERSON_GENDER_INSPECT_POS = ()
PHOTO_PERSON_INSPECT_POS = ()

NAME = ""


country_dict = {
            ARSTOTZKA_COLOR: {
                "name": "Arstotzka",
                "PHOTO_POS": (1920, 1120),
                "GENDER_POS": (2128, 1060),
                "COUNTRY_POS": (1650, 1080),

                "DATE_POS": (2035, 1111, 2288, 1140),
                "CITY_POS": (2108, 1078, 2321, 1106),
                "PHOTO_GENDER_INSPECT_POS": (1810, 780, 2020, 870),
                "PERSON_GENDER_INSPECT_POS": (1260, 865, 1490, 955),
                "PHOTO_PERSON_INSPECT_POS": (1145, 880, 1360, 970)
            },
            ANTEGRIA_COLOR: {
                "name": "Antegria",
                "PHOTO_POS": (2255, 1083),
                "GENDER_POS": (1947, 1073),
                "COUNTRY_POS": (1033, 952),

                "DATE_POS": (1935, 1137, 2115, 1162),
                "CITY_POS": (1935, 1097, 2170, 1127),
                "PHOTO_GENDER_INSPECT_POS": (1870, 745, 2085, 825),
                "PERSON_GENDER_INSPECT_POS": (1180, 870, 1400, 955),
                "PHOTO_PERSON_INSPECT_POS": (1300, 865, 1520, 985)
            },
            OBRISTAN_COLOR: {
                "name": "Obristan",
                "PHOTO_POS": (2250, 1150),
                "GENDER_POS": (1958, 1111),
                "COUNTRY_POS": (1150, 780),

                "DATE_POS": (1945, 1163, 2125, 1190),
                "CITY_POS": (1945, 1130, 2130, 1165),
                "PHOTO_GENDER_INSPECT_POS": (1870, 825, 2100, 900),
                "PERSON_GENDER_INSPECT_POS": (1185, 890, 1400, 970),
                "PHOTO_PERSON_INSPECT_POS": (1300, 900, 1510, 1002)
            },
            IMPOR_COLOR: {
                "name": "Impor",
                "PHOTO_POS": (1920, 1150),
                "GENDER_POS": (2128, 1054),
                "COUNTRY_POS": (1190, 1270),

                "DATE_POS": (2115, 1108, 2325, 1136),
                "CITY_POS": (2115, 1075, 2325, 1105),
                "PHOTO_GENDER_INSPECT_POS": (1810, 780, 2030, 870),
                "PERSON_GENDER_INSPECT_POS": (1260, 860, 1495, 950),
                "PHOTO_PERSON_INSPECT_POS": (1150, 880, 1370, 970)
            },
            KOLECHIA_COLOR: {
                "name": "Kolechia",
                "PHOTO_POS": (1920, 1150),
                "GENDER_POS": (2128, 1095),
                "COUNTRY_POS": (1450, 810),

                "DATE_POS": (2115, 1145, 2300, 1178),
                "CITY_POS": (2115, 1115, 2330, 1143),
                "PHOTO_GENDER_INSPECT_POS": (1810, 815, 2020, 910),
                "PERSON_GENDER_INSPECT_POS": (1260, 875, 1495, 969),
                "PHOTO_PERSON_INSPECT_POS": (1150, 910, 1370, 992)
            },
            UNITEDFED_COLOR: {
                "name": "UnitedFed",
                "PHOTO_POS": (1920, 1150),
                "GENDER_POS": (2128, 1095),
                "COUNTRY_POS": (900, 1220),

                "DATE_POS": (2115, 1144, 2300, 1170),
                "CITY_POS": (2115, 1111, 2315, 1143),
                "PERSON_GENDER_INSPECT_POS": (1260, 875, 1495, 969),
                "PHOTO_PERSON_INSPECT_POS": (1150, 900, 1400, 1000)
            },
            REPUBLIA_COLOR: {
                "name": "Republia",
                "PHOTO_POS": (2250, 1110),
                "GENDER_POS": (1962, 1055),
                "COUNTRY_POS": (1100, 1120),

                "DATE_POS": (1945, 1110, 2125, 1140),
                "CITY_POS": (1945, 1080, 2155, 1105),
                "PHOTO_GENDER_INSPECT_POS": (1875, 770, 2100, 850),
                "PERSON_GENDER_INSPECT_POS": (1185, 860, 1410, 950),
                "PHOTO_PERSON_INSPECT_POS": (1300, 880, 1520, 970)
            }
        }
