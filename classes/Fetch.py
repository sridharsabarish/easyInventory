import  sqlite3
import datetime
import static.Constants as Constants
import logging
from classes.DB import DB

class Fetch:
    def fetchAllInfo(self,forecast=False,searchQuery=None,searchByID=None):
        try:
            print("came here")
            conn = sqlite3.connect(Constants.DB_FILE)
            cursor = conn.cursor()
            # Select all of the items from the database
            if forecast:
                cursor.execute(Constants.QUERY_OLDER_THAN_3_MONTHS)
            else:
                if searchQuery is not None:
                    if searchByID is not None:
                        # Select all of the items from the database
                        cursor.execute(Constants.SEARCH_ID_QUERY, (searchQuery,))
                    else:
                        cursor.execute(Constants.SEARCH_QUERY, (searchQuery,))
                else:
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

