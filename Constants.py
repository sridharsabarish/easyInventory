
from enum import Enum
CSV_FILE='inventory.csv'
DB_FILE='inventory.db'

# SQL Queries

SELECT_ALL="SELECT * FROM inventory"
INSERT_TO_DB="INSERT INTO inventory (item_name, cost, subtype, replacement_duration) VALUES (?, ?, ?, ?)"  # Remember to make this dynamic.
CREATE_TABLE="CREATE TABLE IF NOT EXISTS inventory (item_name TEXT,cost REAL,subtype TEXT,replacement_duration INTEGER)"

SEARCH_QUERY="SELECT * FROM inventory WHERE item_name = ?"
DELETE_ITEM_QUERY="DELETE FROM inventory WHERE item_name = ?"
# Regexes
REGEX_NAME=r'^[a-zA-Z0-9]'
REGEX_NUMBER=r'^\d*$'
regex_map ={"itemName":REGEX_NAME,
      "subtype":REGEX_NAME,
      "cost":REGEX_NUMBER,
      "replacementDuration":REGEX_NUMBER}

#Success
SUCCESS_PRODUCT="These are the products available"
DELETED_PRODUCT="The product has been deleted successfully"
# Errors
ERROR_PRODUCT="'Product not found'"
INVALID_CHOICE="Invalid choice"

#Prompts
DELETE_PRODUCT_PROMPT="Enter the name of product to delete : "

#ACTIONS
class ACTION(Enum):
    INSERT="1"
    DISPLAY="2"
    EXPORT_CSV="3"
    DELETE="4"
    READ_CSV="5"
    EXIT="6"
    SEARCH="8"
    
menuList= [f"{e.value} {e.name}\n" for e in ACTION]
menuString = ''.join(menuList)


# Supported Fields
ITEM_SCHEMA =["itemName","subtype","cost","replacementDuration"];





# New Enum
class EXIT_CODE(Enum):
    SUCCESS = 0
    INVALID = -1