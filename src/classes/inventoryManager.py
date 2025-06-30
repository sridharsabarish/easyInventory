
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from classes.Item import Item
from classes.exportManager import Export2CSV
import static.Constants as Constants, classes.Beautify as Beautify, re, sqlite3
from collections import defaultdict
import tkinter as tk
import logging
import datetime
from classes.DB import DB
from classes.Validation import Validation
from classes.Add import Add
from classes.Delete import Delete
from classes.Edit import Edit
from classes.Fetch import Fetch
logging.basicConfig(filename=Constants.LOG_FILE, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')










if __name__ == "__main__":
    Menu = Menu()
    Menu.handleMenu(choice="")


"""


 Addon Features

1)   Todo :  Calendar API Integration.
    a) Automatic Reminder Feature for items using Google Calendar API
    b) Automatically Delete from Calendar when the item is removed from inventory
    c) Potential integration with GPT to find the average life time for this product after scanning via computer vision and adding it 


# UX Improvements

Todo : Show inventory health using some creative logo.

Todo : Computer Vision, scan an image and automatically prefill the category
    - idea to use Google cloud vision API, this could be fun. #Difficult


# Code Improvements
Todo : Refactoring
- Add Method.





"""

'''



'''