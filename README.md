### Downloader for Scryfall Magic The Gathering Pictures ###

* only for English Card names 

INPUT: List of Magic Card Names without Numbers. Each row only has one Name of 
card. 

OUTPUT: .png files of the Magic Cards from the Input list

Dependencies: 
Python3

HOW TO USE:

1. Create a .txt file with every name of the magic cards of which you want 
to download the pictures from.
2. Therefore put only one name in each row and without numbers like the 
following example: 

file_name.txt: 

Sol Ring
Vindicate 
Black Lotus
[...]

3. Put the file_name.txt file in the same directory as the main.py file
4. Run the python script an the shell with "python3 main.py" 
5. The programm asks you for the name of the .txt file with magic cards you 
want to download from scryfall.com. Type only the filename without the filetype.
So without ".txt"
6. Wait for the Download to finish. 
7. Pictures can be found in folder with the same name as the .txt file.  