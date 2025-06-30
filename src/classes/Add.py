import logging
import static.Constants as Constants
from classes.DB import DB
from classes.exportManager import Export2CSV
from classes.Item import Item
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
