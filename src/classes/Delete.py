import sqlite3
import static.Constants as Constants
import logging


class Delete:
    def deleteData(self, value={}):
        try:
            print("Delete Block")
            logging.debug(value)
            if len(value) == 0:
                id = input(Constants.DELETE_PRODUCT_PROMPT)
            else:
                print("Else of delete")
                logging.debug("Else:" + value[0])
                id=value
                print("Id is :",id)
            conn = sqlite3.connect(Constants.DB_FILE)
            cursor = conn.cursor()
            # Check if the item exists
            cursor.execute(Constants.SEARCH_ID_QUERY, (id,))
            if cursor.fetchone() is None:
                print("Invalid product?")
                logging.error(Constants.ERROR_PRODUCT)
                return Constants.EXIT_CODE.INVALID.value
            else:
                logging.info(Constants.SUCCESS_PRODUCT)
                
            print("Gonna delete : ", id)
            cursor.execute(Constants.DELETE_ITEM_QUERY, (id,))

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
