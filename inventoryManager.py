from Item import Item
from exportManager import Export2CSV
import Constants, Beautify, re, sqlite3
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
            conn = sqlite3.connect(Constants.DB_FILE)
            cursor = conn.cursor()
            # Select all of the items from the database
            cursor.execute(Constants.SELECT_ALL)
            # Initialize an empty dictionary to store the information
            info_list = []
            # Iterate over the rows and collect the information
            for row in cursor.fetchall():
                item_name = row[0]
                cost = row[1]
                subtype = row[2]
                replacement_duration = row[3]
                # Set today's date as the date created
                
                # Todo : Store it in the same DB
                item_date_create = row[4];
                item_date_create = datetime.datetime.strptime(item_date_create, "%Y-%m-%d").date()
                item_date_replacement = item_date_create + datetime.timedelta(days=replacement_duration * 30)
                item_replacement_needed = item_date_replacement < datetime.date.today()

                # Add the information to the dictionary
                info_list.append(
                    {
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
                item_name = row[0]
                cost = row[1]
                subtype = row[2]
                replacement_duration = row[3]
                
                item_date_create = row[4];
                item_date_create = datetime.datetime.strptime(item_date_create, "%Y-%m-%d").date()
                item_date_replacement = item_date_create + datetime.timedelta(days=replacement_duration * 30)
                item_replacement_needed = item_date_replacement < datetime.date.today()
                # Add the information to the dictionary
                info_list.append(
                    {
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
                    item_name = row[0]
                    cost = row[1]
                    subtype = row[2]
                    replacement_duration = row[3]
                    
                    item_date_create = row[4];
                    item_date_create = datetime.datetime.strptime(item_date_create, "%Y-%m-%d").date()
                    item_date_replacement = item_date_create + datetime.timedelta(days=replacement_duration * 30)
                    item_replacement_needed = item_date_replacement < datetime.date.today()
                    # Add the information to the dictionary
                    info_list.append(
                        {
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
                total_cost += row[1]  # Assuming cost is stored in the second column

                counts[row[0].lower()] += 1
                # Check if the current item is the most expensive
                if most_expensive_item is None or row[1] > most_expensive_item[1]:
                    most_expensive_item = row
                # Check if the current item has the shortest replacement duration
                if (
                    shortest_replacement_duration is None
                    or row[3] < shortest_replacement_duration[3]
                ):
                    shortest_replacement_duration = row

            for i in counts.keys():
                print(f"{i}:{counts[i]}")

            Beautify.lineBreak()
            print("Total cost: ${:.2f}".format(total_cost))
            print("Most expensive item: {}".format(most_expensive_item[0]))
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
   def edit():
       # Fill more details.
       return Constants.EXIT_CODE.FAIL.value


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


class Search:
    def search():
        try:
            gui = GUI()
            gui.search()
            return Constants.EXIT_CODE.SUCCESS.value
        except Exception as e:
            logging.error("An error occured:", str(e))
            print("An error occurred:", str(e))
            return Constants.EXIT_CODE.INVALID.value
        return


class Menu:
    def handleMenu(self, choice=""):

        function_dict = {
            Constants.ACTION.DISPLAY.value: Display.display,
            Constants.ACTION.EXPORT_CSV.value: Export2CSV.export2CSV,
            Constants.ACTION.DELETE.value: Delete.deleteData,
            Constants.ACTION.SEARCH.value: Search.search,
        }

        while True:
            if choice == "":
                choice = input(Constants.menuString)
                print(choice)
            elif choice == Constants.ACTION.INSERT.value:
                Add.addItem(inputs={})
                choice = ""
                continue
            elif choice in function_dict:
                function_dict[choice]()
                choice = ""
                continue
            else:
                if choice == Constants.ACTION.EXIT.value:
                    return Constants.EXIT_CODE.SUCCESS.value
                print(Constants.INVALID_CHOICE)
                return Constants.EXIT_CODE.INVALID_CHOICE.value


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Inventory Search")

        self.label = tk.Label(
            self.window, text="Enter the name of the product to be searched:"
        )
        self.label.pack()

        self.entry = tk.Entry(self.window)
        self.entry.pack()

        self.button = tk.Button(self.window, text="Search", command=self.search)
        self.button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        self.table = tk.Text(self.window)
        self.table.pack()

        self.exit_button = tk.Button(
            self.window, text="Exit", command=self.window.destroy
        )
        self.exit_button.pack(side=tk.BOTTOM)

        self.window.mainloop()

    def search(self):
        product_name = self.entry.get()
        conn = sqlite3.connect(Constants.DB_FILE)
        cursor = conn.cursor()
        rows = cursor.execute(Constants.SEARCH_QUERY, (product_name,))
        results = cursor.fetchall()
        conn.close()
        self.result_label.config(text="Search Result:")
        self.table.delete(1.0, tk.END)
        self.table.insert(
            tk.END,
            "{:<20} {:<10} {:<15} {:<20}\n".format(
                "Item Name", "Cost", "Subtype", "Replacement Duration"
            ),
        )
        self.table.insert(tk.END, "-" * 70 + "\n")

        for result in results:
            self.table.insert(
                tk.END,
                "{:<20} {:<10} {:<15} {:<20}\n".format(
                    result[0], result[1], result[2], result[3]
                ),
            )
            self.table.insert(tk.END, "\n")





if __name__ == "__main__":
    Menu = Menu()
    Menu.handleMenu(choice="")


"""

Todo : 

- Move inventory Manager Core features to RUST


Core Features

1) Have a DB to store information.


Luxury Features

1)   Todo :  Calendar API Integration.
    a) Automatic Reminder Feature for items using Google Calendar API
    b) Automatically Delete from Calendar when the item is removed from inventory
    c) Potential integration with GPT to find the average life time for this product after scanning via computer vision and adding it 


2)   Todo : Computer Vision, scan an image and automatically prefill the category
    - idea to use Google cloud vision API, this could be fun.

3)  Todo : Add autocomplete feature for GUI from DB

4) Todo : Show inventory health using some creative logo.







# Need to rework inventory manager's add method, too complex now.





"""

