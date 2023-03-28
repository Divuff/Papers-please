variables = {
    'TEXT_BOX_POSITION': (140, 535),
    'PASSPORT_SIDE_POSITION': (175, 1085),
    'CLOCK_POSITION': (200, 1320),
    'PASSPORT_POSITION': (475, 1085),
    'DOCUMENT_DROP_POSITION': (480, 600),
    'PERSON_POSITION': (490, 850),
    'INTERROGATE_POSITION': (500, 1230),
    'DOCUMENT_AREA_POSITION': (500, 1080),
    'RULE_BOOK_POSITION': (640, 1250),
    'REJECTED_PERSON_LEAVING_POSITION': (700, 450),
    'SPEAKER_POSITION': (830, 370),
    'LEVER_POSITION': (850, 550),
    'BOOKMARK_POSITION': (870, 750),
    'ACCEPTED_PERSON_LEAVING_POSITION': (960, 450),
    'PASSPORT_RULE_POSITION': (1000, 850),
    'RULE_BOOK_SLOT_POSITION': (1300, 1050),
    'ISSUING_CITIES_POSITION': (1400, 1120),
    'DAY_TEST_POSITION': (1444, 180),
    'RULE_BOOK_BASICS_POSITION': (1500, 910),
    'REGIONAL_MAP_POSITION': (1510, 970),
    'REJECTED_STAMP_POSITION': (1600, 695),
    'REJECTED_PASSPORT_POSITION': (1600, 950),
    'PASSPORT_BORDER_POSITION': (1845, 950),
    'PASSPORT_SLOT_POSITION': (2100, 950),
    'APPROVAL_STAMP_POSITION': (2100, 730),
    'APPROVED_PASSPORT_POSITION': (2100, 950),
    'INSPECT_BUTTON_POSITION': (2350, 1320),
    'STAMP_TRAY_POSITION': (2400, 730)
}


def update_position(position):
    x, y = position

    if x < 1280:
        x -= 45
    else:
        x += 125

    x_scale_factor = 1
    y_scale_factor = 1

    if y != 720:
        if y == 1320:
            y_scale_factor = 1440 / 1320
        elif y == 950:
            y_scale_factor = 1070 / 950
        elif y == 370:
            y_scale_factor = 345 / 370

    y = int(y * y_scale_factor)

    return (x, y)


updated_variables = {key: update_position(value) for key, value in variables.items()}

print("Updated variables:")
for key, value in updated_variables.items():
    print(f"{key}: {value}")
