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