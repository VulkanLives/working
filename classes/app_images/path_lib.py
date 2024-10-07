import os

from pathlib2 import Path
pattern_1 = "type1"
pattern_2 = "type2"

list_pattern_1_files = list(Path('/home/chris/PycharmProjects/TTA/app_images').glob(f'**/*.{pattern_1}'))
list_pattern_2_files = list(Path('/home/chris/PycharmProjects/TTA/app_images').glob(f'**/*.{pattern_2}'))
files = [ f for f in os.listdir('/home/chris/PycharmProjects/TTA/app_images') if f.endswith('.png') ]

files.

print(pattern_1)
print(pattern_2)
print(files)