import re
import static.Constants as Constants

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

