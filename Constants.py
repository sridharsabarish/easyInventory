
CSV_FILE='inventory.csv'
DB_FILE='inventory.db'

# SQL Queries

SELECT_ALL="SELECT * FROM inventory"
INSERT_TO_DB="INSERT INTO inventory (item_name, cost, subtype, replacement_duration) VALUES (?, ?, ?, ?)"
CREATE_TABLE="CREATE TABLE IF NOT EXISTS inventory (item_name TEXT,cost REAL,subtype TEXT,replacement_duration INTEGER)"

SEARCH_QUERY="SELECT * FROM inventory WHERE item_name = ?"
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


#ACTIONS
ACTION_INSERT="1"
ACTION_DISPLAY="2"
ACTION_EXPORT_CSV="3"
ACTION_DELETE="4"
ACTION_READ_CSV="5"
ACTION_EXIT="6"
ACTION_SEARCH="8"
