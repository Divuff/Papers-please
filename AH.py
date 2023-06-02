
from BackEndUpdate import *

from Text_Detection import find_two_word_coordinates, find_word_coordinates


print(find_word_coordinates('IMMIGRATE'))




Id = find_two_word_coordinates('VIMLI', 'DESHOVSKI')
print(textdetect(Id))


print(f"'Passport_id_pos': {Id}")