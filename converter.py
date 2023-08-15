# Basic Library Imports
import os
import sys
from PIL import Image

# Grab the first and second arguments as from the command line
main_folder = sys.argv[1]
new_folder = sys.argv[2]

# To check if the new folder actually exists
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# Loop through the Pkoemons folder, reassign the format to the images and save in the New Pokemosn folder
for filename in os.listdir(main_folder):
    img = Image.open(f'{main_folder}{filename}')
    new_name = os.path.splitext(filename)[0]
    print(new_name)
    img.save(f'{new_folder}{new_name}.png', 'png')
    
    # A little checker
    print('Done!')