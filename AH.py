
old_resolution = (2275, 1278)
new_resolution = (2560, 1440)


def update_coordinates_v5(old_coord, old_resolution, new_resolution):
    old_x, old_y = old_coord
    old_width, old_height = old_resolution
    new_width, new_height = new_resolution

    half_old_width, half_old_height = old_width / 2, old_height / 2
    half_new_width, half_new_height = new_width / 2, new_height / 2

    x_scale = half_new_width / half_old_width
    y_scale = half_new_height / half_old_height

    new_x = half_new_width + (old_x - half_old_width) * x_scale
    new_y = half_new_height + (old_y - half_old_height) * y_scale

    return (int(new_x), int(new_y))


old_coordinates = {
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
    'PASSPORT_BORDER_POSITION': (1845, 950),
    'PASSPORT_SLOT_POSITION': (2100, 950),
    'APPROVAL_STAMP_POSITION': (2100, 730),
    'APPROVED_PASSPORT_POSITION': (2100, 950),
    'INSPECT_BUTTON_POSITION': (2350, 1320),
    'STAMP_TRAY_POSITION': (2400, 730)
}

new_coordinates = {}
for name, old_coord in old_coordinates.items():
    new_coordinates[name] = update_coordinates_v5(old_coord, old_resolution, new_resolution)

# Print the updated coordinates
for name, new_coord in new_coordinates.items():
    print(f"{name}: {new_coord}")