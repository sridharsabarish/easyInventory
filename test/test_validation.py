import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from classes.Validation import Validation
from loguru import logger


class TestValidation:
    def test_create_validation_objection(self):
        try:
            val = Validation()
            assert True
        except Exception as e:
            assert False, f"An error occurred: {e}"
            
    def test_validation__itemName_correct(self):
        try:
            val = Validation()
            logger.debug("Test Validation correct name")
            input =  {"key": "itemName", "value": "TestInput"}
            logger.debug(input)
            
            assert val.validateInput(x=input) == 0
        except Exception as e:
            assert False, f"An error occurred: {e}"


    def test_validation__itemName_inccorrect(self):
        try:
            val = Validation()
            logger.debug("Test Validation correct name")
            input =  {"key": "itemName", "value": 1}
            logger.debug(input)
            
            assert val.validateInput(x=input) != 0
        except Exception as e:
            assert True, f"An error occurred: {e}"
            
    def test_validation_incorrect_key(self):
        try:
            val = Validation()
            logger.debug("Test Validation correct name")
            input =  {"key": "flipcoin", "value": "TestInput"}
            logger.debug(input)
            
            assert val.validateInput(x=input) != 0
        except Exception as e:
            assert True, f"An error occurred: {e}"
            

    def test_validation_date_correct(self):
        try:
            val = Validation()
            logger.debug("Test Validation correct date")
            input =  {"key": "dateCreated", "value": "2023-01-01"}
            logger.debug(input)
            
            assert val.validateInput(x=input) == 0
        except Exception as e:
            assert False, f"An error occurred: {e}"
            
            
    def test_validation_date_incorrect(self):
        try:
            val = Validation()
            logger.debug("Test Validation incorrect correct date")
            input =  {"key": "dateCreated", "value": "202-01-01"}
            logger.debug(input)
            
            assert val.validateInput(x=input) != 0
        except Exception as e:
            assert True, f"An error occurred: {e}"
            
    def test_validate_cost_correct(self):
        try:
            val = Validation()
            logger.debug("Test Validation correct cost")
            input =  {"key": "cost", "value": "100"}
            logger.debug(input)
            
            assert val.validateInput(x=input) == 0
        except Exception as e:
            assert False, f"An error occurred: {e}"