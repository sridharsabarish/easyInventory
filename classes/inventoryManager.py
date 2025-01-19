from classes.Item import Item
from classes.exportManager import Export2CSV
import static.Constants as Constants, classes.Beautify as Beautify, re, sqlite3
from collections import defaultdict
import tkinter as tk
import logging
import datetime


logging.basicConfig(filename=Constants.LOG_FILE, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
class DB:

    def createTable():

        try:
            conn = sqlite3.connect(Constants.DB_FILE)
            cursor = conn.cursor()
            cursor.execute(Constants.CREATE_TABLE)
            logging.info(Constants.SUCCESS_TABLE)
            conn.commit()
            conn.close()
            return Constants.EXIT_CODE.SUCCESS.value
        except Exception as e:
            logging.error(Constants.ERROR_CREATE_TABLE, str(e))
            print(Constants.ERROR_CREATE_TABLE, str(e))
            return Constants.EXIT_CODE.INVALID.value

    def saveToDB(item):
        conn = sqlite3.connect(Constants.DB_FILE)
        cursor = conn.cursor()
        # Create the table if it doesn't exist
        cursor.execute(Constants.CREATE_TABLE)
        logging.info(Constants.SUCCESS_TABLE)
        # Save the variables to the database
        cursor.execute(
            Constants.INSERT_TO_DB,
            (
                item.getItemName(),
                item.getCost(),
                item.getSubtype(),
                item.getReplacementDuration(),
                item.getDateCreated(),
                item.getDateOfReplacement()
            ),
        )
        logging.info(Constants.SUCCESS_ITEM)
        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        
    def updateDB(id, item):
        conn = sqlite3.connect(Constants.DB_FILE)
        cursor = conn.cursor()
        # Check if the id exists
        cursor.execute(
            """
            SELECT COUNT(*) FROM inventory
            WHERE id = ?
            """,
            (id,)
        )
        if cursor.fetchone()[0] == 0:
            logging.error("ID does not exist")
            raise Exception("ID does not exist")
        # Update the variables to the database
        cursor.execute(
            """
            UPDATE inventory
            SET item_name = ?, cost = ?, subtype = ?, replacement_duration = ?, dateCreated = ?, dateOfReplacement = ?
            WHERE id = ?
            """,
            (
                item.getItemName(),
                item.getCost(),
                item.getSubtype(),
                item.getReplacementDuration(),
                item.getDateCreated(),
                item.getDateOfReplacement(),
                id
            ),
        )
        logging.info(Constants.SUCCESS_ITEM)
        # Commit the changes and close the connection
        conn.commit()
        conn.close()

class Validation:
    """

    Validate an input based on its data type.

    """

    def validateInput(x) -> str:
        try:
            data_type = x["key"]
            value = x["value"]
            pattern = re.compile(Constants.regex_map[data_type])
            if bool(pattern.match(value)):
                return Constants.EXIT_CODE.SUCCESS.value
            else:
                logging.debug(Constants.INVALID_INPUT)
                return Constants.EXIT_CODE.INVALID.value
        except Exception as e:
            print(Constants.ERROR_VALIDATION, str(e))
            logging.error(Constants.ERROR_VALIDATION, str(e))
            return Constants.EXIT_CODE.INVALID.value


class Add:
    def addItem(self, inputs={}):
        val = {}
        logging.debug(len(inputs))
        logging.debug(inputs)
        if len(inputs) != 6:
            for i in range(0, len(Constants.ITEM_SCHEMA)):

                initialInput = input(f"Enter {Constants.ITEM_SCHEMA[i]} : ")
                # x=Validation.validateInput(Constants.ITEM_SCHEMA[i]);

                val[i] = initialInput
        else:
            # Todo : validate output
            val = inputs
        newItem = Item(*val.values())
        # Connect to the database
        DB.saveToDB(newItem)
        Export2CSV.export2CSV()
        return 0


class Fetch:
    def fetchAllInfo(self):
        try:
            print("came here")
            conn = sqlite3.connect(Constants.DB_FILE)
            cursor = conn.cursor()
            # Select all of the items from the database
            cursor.execute(Constants.SELECT_ALL)
            # Initialize an empty dictionary to store the information
            info_list = []
            # Iterate over the rows and collect the information
            
            for row in cursor.fetchall():
                print(row) 
                print("There there")
                id=row[0]
                item_name = row[1]
                cost = row[2]
                subtype = row[3] 
                replacement_duration = row[4] 
                # Set today's date as the date created
                
                # Todo : Store it in the same DB
                item_date_create = row[5];
                item_date_create = datetime.datetime.strptime(item_date_create, "%Y-%m-%d").date()
                item_date_replacement = item_date_create + datetime.timedelta(days=replacement_duration * 30)
                item_replacement_needed = item_date_replacement < datetime.date.today()

                # Add the information to the dictionary
                info_list.append(
                    {
                        Constants.ITEM.ID: id,
                        Constants.ITEM.NAME: item_name,
                        Constants.ITEM.COST: cost,
                        Constants.ITEM.TYPE: subtype,
                        Constants.ITEM.DURATION: replacement_duration,
                        Constants.ITEM.CREATION_DATE: item_date_create,
                        Constants.ITEM.REPLACEMENT_DATE: item_date_replacement,
                        "needsReplacement": item_replacement_needed
                    }
                )

            logging.debug(info_list)
            # Close the connection
            conn.close()
            return info_list
        except Exception as e:
            print(Constants.ERROR_FETCH, str(e))
            logging.error(Constants.ERROR_FETCH, str(e))
            return {}
    def fetchInfo(self,searchQuery):
        try:
            conn = sqlite3.connect(Constants.DB_FILE)
            cursor = conn.cursor()
            # Select all of the items from the database
            cursor.execute(Constants.SEARCH_QUERY, (searchQuery,))
            # Initialize an empty dictionary to store the information
            info_list = []
            # Iterate over the rows and collect the information

            for row in cursor.fetchall():
                id = row[0]
                item_name = row[1]
                cost = row[2]
                subtype = row[3]
                replacement_duration = row[4]
                
                item_date_create = row[5];
                item_date_create = datetime.datetime.strptime(item_date_create, "%Y-%m-%d").date()
                item_date_replacement = item_date_create + datetime.timedelta(days=replacement_duration * 30)
                item_replacement_needed = item_date_replacement < datetime.date.today()
                # Add the information to the dictionary
                info_list.append(
                    {
                        Constants.ITEM.ID: id,
                        Constants.ITEM.NAME: item_name,
                        Constants.ITEM.COST: cost,
                        Constants.ITEM.TYPE: subtype,
                        Constants.ITEM.DURATION: replacement_duration,
                        Constants.ITEM.CREATION_DATE: item_date_create,
                        Constants.ITEM.REPLACEMENT_DATE: item_date_replacement,
                        "needsReplacement": item_replacement_needed
                    }
                )
                
            logging.debug(info_list)
            # Close the connection
            conn.close()
            return info_list
        except Exception as e:
            print(Constants.ERROR_FETCH, str(e))
            logging.error(Constants.ERROR_FETCH, str(e))
            return {}

    def fetchInfoFiltered(self):
            try:
                conn = sqlite3.connect(Constants.DB_FILE)
                cursor = conn.cursor()
                # Select all of the items from the database
                cursor.execute(Constants.QUERY_OLDER_THAN_TODAY)
                # Initialize an empty dictionary to store the information
                info_list = []
                # Iterate over the rows and collect the information

                for row in cursor.fetchall():
                    id=row[0]
                    item_name = row[1]
                    cost = row[2]
                    subtype = row[3]
                    replacement_duration = row[4]
                    
                    item_date_create = row[5];
                    item_date_create = datetime.datetime.strptime(item_date_create, "%Y-%m-%d").date()
                    item_date_replacement = item_date_create + datetime.timedelta(days=replacement_duration * 30)
                    item_replacement_needed = item_date_replacement < datetime.date.today()
                    # Add the information to the dictionary
                    info_list.append(
                        {
                            Constants.ITEM.ID: id,
                            Constants.ITEM.NAME: item_name,
                            Constants.ITEM.COST: cost,
                            Constants.ITEM.TYPE: subtype,
                            Constants.ITEM.DURATION: replacement_duration,
                            Constants.ITEM.CREATION_DATE: item_date_create,
                            Constants.ITEM.REPLACEMENT_DATE: item_date_replacement,
                            "needsReplacement": item_replacement_needed
                        }
                    )

                logging.debug(info_list)
                # Close the connection
                conn.close()
                return info_list
            except Exception as e:
                print(Constants.ERROR_FETCH, str(e))
                logging.error(Constants.ERROR_FETCH, str(e))
                return {}


class Display:
    def display():
        try:
            conn = sqlite3.connect(Constants.DB_FILE)
            cursor = conn.cursor()

            # Select all of the items from the database
            cursor.execute(Constants.SELECT_ALL)
            # Initialize variables for most expensive item and shortest replacement duration
            most_expensive_item = None
            shortest_replacement_duration = None

            counts = defaultdict(int)
            # Keep count of all the items
            # Print the items
            total_cost = 0
            for row in cursor.fetchall():
                if row is None:
                    break

                print(row)
                total_cost += row[2]  # Assuming cost is stored in the second column

                counts[row[0].lower()] += 1
                # Check if the current item is the most expensive
                if most_expensive_item is None or row[2] > most_expensive_item[1]:
                    most_expensive_item = row
                # Check if the current item has the shortest replacement duration
                if (
                    shortest_replacement_duration is None
                    or row[4] < shortest_replacement_duration[4]
                ):
                    shortest_replacement_duration = row

            for i in counts.keys():
                print(f"{i}:{counts[i]}")

            Beautify.lineBreak()
            print("Total cost: ${:.2f}".format(total_cost))
            print("Most expensive item: {}".format(most_expensive_item[1]))
            print(
                "Item with shortest replacement duration: {}".format(
                    shortest_replacement_duration[0]
                )
            )
            Beautify.lineBreak()

            # Close the connection
            conn.close()
            return Constants.EXIT_CODE.SUCCESS.value
        except Exception as e:
            print(Constants.ERROR_DISPLAY, str(e))
            return Constants.EXIT_CODE.INVALID.value
class Edit:
   def editItem(self, id, inputs={}):
        val = {}
        logging.debug(len(inputs))
        logging.debug(inputs)
        if len(inputs) != 6:
            for i in range(0, len(Constants.ITEM_SCHEMA)):

                initialInput = input(f"Enter {Constants.ITEM_SCHEMA[i]} : ")
                # x=Validation.validateInput(Constants.ITEM_SCHEMA[i]);

                val[i] = initialInput
        else:
            # Todo : validate output
            val = inputs
        try:
            newItem = Item(*val.values())
            # Connect to the database
            DB.updateDB(id,newItem)
            Export2CSV.export2CSV()
        except Exception as e:
            print("Error is ", e)
            return Constants.EXIT_CODE.FAIL.value
        return Constants.EXIT_CODE.SUCCESS.value
       




class Delete:
    def deleteData(self, value={}):
        try:
            logging.debug(value)
            if len(value) == 0:
                name = input(Constants.DELETE_PRODUCT_PROMPT)
            else:
                logging.debug("Else:" + value[0])
                name=value
                logging.debug("name : ", name)
            conn = sqlite3.connect(Constants.DB_FILE)
            cursor = conn.cursor()
            # Check if the item exists
            cursor.execute(Constants.SEARCH_QUERY, (name,))
            if cursor.fetchone() is None:
                logging.error(Constants.ERROR_PRODUCT)
                return Constants.EXIT_CODE.INVALID.value
            else:
                logging.info(Constants.SUCCESS_PRODUCT)
            cursor.execute(Constants.DELETE_ITEM_QUERY, (name,))

            conn.commit()
            conn.close()
            logging.info(Constants.DELETED_PRODUCT)
            print(Constants.DELETED_PRODUCT)
            return Constants.EXIT_CODE.SUCCESS.value
            # Export2CSV.export2CSV()
        except Exception as e:
            logging.error(Constants.ERROR_DELETE, str(e))
            print(Constants.ERROR_DELETE, str(e))
        return Constants.EXIT_CODE.INVALID.value


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