import re
import static.Constants as Constants
from loguru import logger

class Validation:
    """

    Validate an input based on its data type.

    """

    def validateInput(self,x) -> int:
        try:
            logger.debug("The object x is ", x)
            data_type = x["key"]
            value = x["value"]
            logger.debug("Data type is ", data_type)
            logger.debug("Value is ", value)
            logger.debug("Pattern is ", Constants.regex_map[data_type])
            pattern = re.compile(Constants.regex_map[data_type])
            if bool(pattern.match(value)):
                logger.success("Pattern matching worked")
                return Constants.EXIT_CODE.SUCCESS.value
            else:
                logger.error("Invalid input")
                logger.debug(Constants.INVALID_INPUT)
                return Constants.EXIT_CODE.INVALID.value
        except Exception as e:
            logger.error(Constants.ERROR_VALIDATION, str(e))
            logger.error(Constants.ERROR_VALIDATION, str(e))
            return Constants.EXIT_CODE.INVALID.value

