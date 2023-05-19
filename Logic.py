from Colors import ARSTOTZKA_COLOR, \
    ANTEGRIA_COLOR, OBRISTAN_COLOR, UNITEDFED_COLOR, REPUBLIA_COLOR, IMPOR_COLOR, KOLECHIA_COLOR

PersonPresent = False
PassportPresent = False
StampingTime = False
NoPassport = False
NextPerson = False
CorrectDate = False
CorrectCity = False
PersonGenderMatch = False
PhotoPersonMatch = False
TicketPresent = False
ValidTicket = False
DocumentStatus = False
NoTicket = False
TextBoxPresent = False
Arstotzkan = False

DATE_POSITION = ()
PHOTO_POSITION = ()
CITY_POSITION = ()
GENDER_POSITION = ()

COUNTRY_POSITION = ()
PHOTO_GENDER_INSPECT_POSITION = ()
PERSON_GENDER_INSPECT_POSITION = ()
PHOTO_PERSON_INSPECT_POSITION = ()

NAME = ""

country_dict = {
            ARSTOTZKA_COLOR: {
                "name": "Arstotzka",
                "PHOTO_POSITION": (1920, 1120),
                "GENDER_POSITION": (2128, 1060),
                "COUNTRY_POSITION": (1650, 1080),

                "DATE_POSITION": (2035, 1111, 2288, 1140),
                "CITY_POSITION": (2108, 1078, 2321, 1106),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 780, 2020, 870),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 865, 1490, 955),
                "PHOTO_PERSON_INSPECT_POSITION": (1145, 880, 1360, 970)
            },
            ANTEGRIA_COLOR: {
                "name": "Antegria",
                "PHOTO_POSITION": (2255, 1083),
                "GENDER_POSITION": (1947, 1073),
                "COUNTRY_POSITION": (1033, 952),

                "DATE_POSITION": (1935, 1137, 2115, 1162),
                "CITY_POSITION": (1935, 1097, 2170, 1127),
                "PHOTO_GENDER_INSPECT_POSITION": (1870, 745, 2085, 825),
                "PERSON_GENDER_INSPECT_POSITION": (1180, 870, 1400, 955),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 865, 1520, 985)
            },
            OBRISTAN_COLOR: {
                "name": "Obristan",
                "PHOTO_POSITION": (2250, 1150),
                "GENDER_POSITION": (1958, 1111),
                "COUNTRY_POSITION": (1150, 780),

                "DATE_POSITION": (1945, 1163, 2125, 1190),
                "CITY_POSITION": (1945, 1130, 2130, 1165),
                "PHOTO_GENDER_INSPECT_POSITION": (1870, 825, 2100, 900),
                "PERSON_GENDER_INSPECT_POSITION": (1185, 890, 1400, 970),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 900, 1510, 1002)
            },
            IMPOR_COLOR: {
                "name": "Impor",
                "PHOTO_POSITION": (1920, 1150),
                "GENDER_POSITION": (2128, 1054),
                "COUNTRY_POSITION": (1190, 1270),

                "DATE_POSITION": (2115, 1108, 2325, 1136),
                "CITY_POSITION": (2115, 1075, 2325, 1105),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 780, 2030, 870),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 860, 1495, 950),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 880, 1370, 970)
            },
            KOLECHIA_COLOR: {
                "name": "Kolechia",
                "PHOTO_POSITION": (1920, 1150),
                "GENDER_POSITION": (2128, 1095),
                "COUNTRY_POSITION": (1450, 810),

                "DATE_POSITION": (2115, 1145, 2300, 1178),
                "CITY_POSITION": (2115, 1115, 2330, 1143),
                "PHOTO_GENDER_INSPECT_POSITION": (1810, 815, 2020, 910),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 875, 1495, 969),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 910, 1370, 992)
            },
            UNITEDFED_COLOR: {
                "name": "UnitedFed",
                "PHOTO_POSITION": (1920, 1150),
                "GENDER_POSITION": (2128, 1095),
                "COUNTRY_POSITION": (900, 1220),

                "DATE_POSITION": (2115, 1144, 2300, 1170),
                "CITY_POSITION": (2115, 1111, 2315, 1143),
                "PERSON_GENDER_INSPECT_POSITION": (1260, 875, 1495, 969),
                "PHOTO_PERSON_INSPECT_POSITION": (1150, 900, 1400, 1000)
            },
            REPUBLIA_COLOR: {
                "name": "Republia",
                "PHOTO_POSITION": (2250, 1110),
                "GENDER_POSITION": (1962, 1055),
                "COUNTRY_POSITION": (1100, 1120),

                "DATE_POSITION": (1945, 1110, 2125, 1140),
                "CITY_POSITION": (1945, 1080, 2155, 1105),
                "PHOTO_GENDER_INSPECT_POSITION": (1875, 770, 2100, 850),
                "PERSON_GENDER_INSPECT_POSITION": (1185, 860, 1410, 950),
                "PHOTO_PERSON_INSPECT_POSITION": (1300, 880, 1520, 970)
            }
        }

