import sqlite3
import static.Constants as Constants
import logging


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
