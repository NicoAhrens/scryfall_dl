# import for waiting a while for every request to not overload scryfall server
import time
# for getting the path of files and create a save folder
import os

# request for using urls in the script
from requests import get
# reading out json files for finding the right card in the list
from json import loads
# for saving the found card in the end to a png file
from shutil import copyfileobj

from pathlib import Path

# creating neccessary variables
# save_folder is the current workind directory
save_folder = os.path.join(os.getcwd())
# Input from the User for reading the right file
read_file = input('Type in the name of the file without the ".txt" (case sensitive)\n> ')
# creating the file name for reading it out
read_file_type = read_file + '.txt'
if not os.path.isdir(read_file):
    os.mkdir(read_file)
# reads out every line of the .txt file and puts them into a list
with open(read_file_type) as f:
    lines = f.read().splitlines()


for image in range(len(lines)):
    time.sleep(0.1)
    # Load the card data from Scryfall
    card = loads(get(f"https://api.scryfall.com/cards/search?q={lines[image]}").text)
    # print(card)
    # Get the image URL
    # print(lines[image])
    for image_id in range(len(card['data'])):
        # print(image_id)
        card_path_name = card['data'][image_id]['name']
        if card_path_name == lines[image]:
            img_url = card['data'][image_id]['image_uris']['png']

    # creates a f
    file_save_name = os.path.join(save_folder, read_file, lines[image])

    # saving the image into the right folder

    if Path(f'{file_save_name}.png').exists():
        # file exists
        print(f"Allready downloaded: {card_path_name}")
    else:
        with open(f'{file_save_name}.png', 'wb') as out_file:
            copyfileobj(get(img_url, stream=True).raw, out_file)
            print(f"Download complete for: {card_path_name}")
