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

NoIdCard = False

IdCardPresent = False
ValidEntryPermit = False
ValidIdCardName = False
ValidIdCardDistrict = False
ValidIdCardPhoto = False
NoEntryPermit = False
EntryPermitPresent = False
ValidEntryPermitID = False
ValidEntryPermitDate = False
ValidEntryPermitDuration = False
ValidEntryPermitName = False
ValidEntryPermitPurpose = False
Foreigner = False

Approved = False
Rejected = False

ValidIdCard = False

purpose_dict = {
    "immigrate":{
    "immigrating",
    "live with",
    "i will move"
    },
    "visit":{
    "visit",
    "visiting"
    },
    "transit":{
    "transit"
    
    }

}

time_length_dict = {
"2 days": {
"2 days",
"14 days",
"forty-eight hours",
"couple days"
},
"1 week": {
"1 week",
"7 days",
"seven days",
"a week"
},
"14 days": {
"2 weeks",
"14 days",
"fourteen days",
"a couple of weeks"
},
"1 month": {
"1 month",
"30 days",
"thirty days",
"4 weeks",
"four weeks"
},
"2 months": {
"2 months",
"8 weeks",
"a couple of months",
"two months"
},
"3 months": {
"3 months",
"90 days",
"12 weeks",
"quarter of a year"
},
"6 months": {
"6 months",
"180 days",
"one hundred eighty days",
"half a year"
},
"1 year": {
"1 year",
"365 days",
"three hundred sixty-five days",
"twelve months"
},
"forever": {
"immigrating",
"live with",
"i will move",
"twelve months"
}

}




