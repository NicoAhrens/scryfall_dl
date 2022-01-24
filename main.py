# import for waiting a while for every request to not overload scryfall server
import time
# for getting the path of files and create a save folder
import os

# request for using urls in the script
from requests import get
# reading out json files for finding the right card in the list
from json import loads
# for saving the found card at the end to a png file
from shutil import copyfileobj

from pathlib import Path

# Creating neccessary variables
# save_folder is the current workind directory, for easier use of path in
# following code
save_folder = os.path.join(os.getcwd())
# Input from the User. read_file saves the name of the while, which the user
# wants to put into the script
read_file = input('Type in the name of the file without the ".txt" (case sensitive)\n> ')
# Creating the file name with the .txt extension for reading it out
# with splitlines()
read_file_type = read_file + '.txt'
# Creates a folder with the name of the given list to save the pictures of the
# cards
if not os.path.isdir(read_file):
    os.mkdir(read_file)
# Reads out every line of the .txt file and puts them into a list
with open(read_file_type) as f:
    lines = f.read().splitlines()

# Iteration over every card from the list and searching for it on the scryfall
# site.
for image in range(len(lines)):
    # time.sleep to not overload the server of the scryfall with requests
    time.sleep(0.1)
    # Load the card data from Scryfall
    card = loads(get(f"https://api.scryfall.com/cards/search?q={lines[image]}").text)
    # checking if the first card which is found with the query, if its the right
    # one. For e.g. for the query "Black Lotus", the first card in the output
    # is "Blacker Lotus" and the second one is "Black Lotus"
    for image_id in range(len(card['data'])):
        card_path_name = card['data'][image_id]['name']
        if card_path_name == lines[image]:
            img_url = card['data'][image_id]['image_uris']['png']

    # creates a save name for the file within the created savefolder with
    # save_folder and read_file. The filename is given with the name of the
    # searched card nam with lines[image]
    file_save_name = os.path.join(save_folder, read_file, lines[image])

    # saving the image into the right folder
    # checks if the card allready exists and if not saves it with the given
    # file_save_name as an .png
    if Path(f'{file_save_name}.png').exists():
        # gives out a statement for the user if the given card is allready
        # downloaded
        print(f"Allready downloaded: {card_path_name}")
    else:
        with open(f'{file_save_name}.png', 'wb') as out_file:
            copyfileobj(get(img_url, stream=True).raw, out_file)
            # gives out a statement for the user if the download is finished
            # for the given card
            print(f"Download complete for[{image+1}/{len(lines)}] : {card_path_name}")
