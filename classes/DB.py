import sqlite3
import static.Constants as Constants
import logging
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
