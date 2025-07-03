import logging
import static.Constants as Constants
from classes.DB import DB
from classes.exportManager import Export2CSV
from classes.Item import Item
from classes.Validation import Validation
from loguru import logger
class Add:
    def addItem(self, inputs={}):
        val = {}
        logger.debug("Adding item")
        logger.debug("Adding item: ",inputs)
        logger.debug("Input length ",len(inputs))
 
        if len(inputs) != 6:
            for i in range(0, len(Constants.ITEM_SCHEMA)):

                initialInput = input(f"Enter {Constants.ITEM_SCHEMA[i]} : ")
                logger.debug("Input from user")
                try:
                    inputToTest =  {"key": Constants.ITEM_SCHEMA[i], "value": initialInput}
                    logger.debug("Trying to validate the input")
                    Validation.validateInput(inputToTest);
                except Exception as e:
                    logger.error("Error is ", e)
                    return Constants.EXIT_CODE.INVALID.value

                val[i] = initialInput
        else:
            # Todo : validate output
            val = inputs
        newItem = Item(*val.values())
        # Connect to the database
        DB.saveToDB(newItem)
        Export2CSV.export2CSV()
        return 0
