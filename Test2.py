from BackEndUpdate import *
from Colors import ARSTOTZKA_COLOR, ENTRY_PERMIT_COLOR2, TEXTBOX_COLOR, DAY_COLOR, DOCUMENT_AREA_COLOR, WALL_COLOR, IDCARD_COLOR, \
    ENTRY_PERMIT_COLOR

from Pos import positions
import time
from Logic import *

Passport_border_pos = (1633, 729)

country = get_image_color(Passport_border_pos)
country_data = set_country_positions(country)
            
test_compare_pos_text(country_data['Passport_id_pos'], positions['Entry_permit_id_pos'])

