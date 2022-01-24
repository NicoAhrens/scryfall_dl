# MTG Card Picture Downloader for Scryfall API 

* only for English Card names 

## WHAT DOES THE SCRIPT
With this Python script you can download a set of MTG card pictures with a deck list from [Scryfall.com](https://scryfall.com/)

## INPUT: 
List of MTG card names without numbers. Each row only has one name of card with no trailing whitespace.

## OUTPUT: 
`<card_name>.png ` files of the Magic Cards from the Input list

## HOW TO USE:

1. Create a .txt file with every name of the magic cards of which you want 
to download the pictures from.
2. Therefore put only one name in each row and without numbers like the 
following example. Be aware of trailing whitespace.

`<name>.txt`: 
Sol Ring<br />
Vindicate<br />
Black Lotus<br />
[...]

3. Put the `<name>.txt` file in the same directory as the `main.py` file
4. First run the terminal in the same path as the `main.py.` Or run it with the full path name. Run the python script in the shell with `$ python3 main.py`.
5. The programm asks you for the name of the `<name>.txt` file with magic cards you want to download from scryfall.com. 
Type only the filename without the filetype (without ".txt") into the command prompt.
6. Wait for the Download to finish.
7. Pictures can be found in folder with the same name as the .txt file.
