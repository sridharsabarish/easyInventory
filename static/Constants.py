from enum import Enum

CSV_FILE = "inventory.csv"
DB_FILE = "inventory.db"
LOG_FILE="app.log"

# SQL Queries

SELECT_ALL = "SELECT * FROM inventory"
INSERT_TO_DB = "INSERT INTO inventory (item_name, cost, subtype, replacement_duration,dateCreated,dateOfReplacement) VALUES (?, ?, ?, ?,?,?)"  # Remember to make this dynamic.
CREATE_TABLE = "CREATE TABLE IF NOT EXISTS inventory (id integer primary key autoincrement,item_name TEXT, cost REAL, subtype TEXT, replacement_duration INTEGER, dateCreated DATE, dateOfReplacement DATE)"

SEARCH_QUERY = "SELECT * FROM inventory WHERE item_name = ?"
SEARCH_ID_QUERY = "SELECT * FROM inventory WHERE id = ?"
QUERY_OLDER_THAN_TODAY = "SELECT * FROM inventory WHERE dateOfReplacement < date('now')"
QUERY_OLDER_THAN_3_MONTHS = "SELECT * FROM inventory WHERE dateOfReplacement < date('now','3 month')"
DELETE_ITEM_QUERY = "DELETE FROM inventory WHERE id = ?"
# Regexes
REGEX_NAME = r"^[a-zA-Z]"
REGEX_NUMBER = r"^\d*$"
regex_map = {
    "itemName": REGEX_NAME,
    "subtype": REGEX_NAME,
    "cost": REGEX_NUMBER,
    "replacementDuration": REGEX_NUMBER,
}

# Success
SUCCESS_PRODUCT = "These are the products available"
DELETED_PRODUCT = "The product has been deleted successfully"
SUCCESS_TABLE = "Table created successfully"
SUCCESS_ITEM = "Item added successfully"
# Errors
ERROR_PRODUCT = "'Product not found'"
INVALID_CHOICE = "Invalid choice"
INVALID_INPUT = "Invalid input"
ERROR_VALIDATION = "An error occurred while validating the input: "
ERROR_DELETE = "An error occurred while deleting the product:"
ERROR_DISPLAY = "An error occurred while displaying the items:"
ERROR_FETCH = "An error occurred while fetching the items:"
ERROR_CREATE_TABLE = "An error occurred while creating the table:"
ERROR_EDIT_NOT_FOUND="Item not found to be edited"
# Prompts
DELETE_PRODUCT_PROMPT = "Enter the name of product to delete : "
EDIT_PRODUCT_PROMPT = "Enter the name of product to edit : "

# ACTIONS
class ACTION(Enum):
    INSERT = "1"
    DISPLAY = "2"
    EXPORT_CSV = "3"
    DELETE = "4"
    READ_CSV = "5"
    EXIT = "6"
    SEARCH = "8"


menuList = [f"{e.value} {e.name}\n" for e in ACTION]
menuString = "".join(menuList)


# Supported Fields
ITEM_SCHEMA = ["itemName", "subtype", "cost", "replacementDuration","dateCreated","dateOfReplacement"]


# New Enum
class EXIT_CODE(Enum):
    SUCCESS = 0
    INVALID = -1


# Input validation
ALLOWED_SUBTYPES = ["Electronics", "Clothes", "Books", "Household"]


class ITEM:
    ID="id"
    NAME = "name"
    TYPE = "subtype"
    COST = "cost"
    DURATION = "replacementDuration"
    CREATION_DATE = "dateCreated"
    REPLACEMENT_DATE = "dateOfReplacement"
    
    
# UX
INVENTORY_PAGE="inventory.html"
ADD_PAGE="add.html"
ERROR_PAGE="error.html"
DELETE_PAGE="delete.html"
DISPLAY_PAGE="display.html"
SEARCH_PAGE="search.html"
EDIT_PAGE="edit.html"
INDEX_PAGE="index.html"

