import unittest
from classes.inventoryManager import  Add, Display, Delete, Validation, DB, Edit
from classes.exportManager import Export2CSV
import static.Constants as Constants
import datetime

class TestInventoryManager(unittest.TestCase):

  
    handleInputs = Add()
    export2csv = Export2CSV()
    display = Display()
    delete = Delete()
    edit = Edit()

    def testCreateEmptyDB(self):
        out = DB.createTable()
        self.assertEqual(out, Constants.EXIT_CODE.SUCCESS.value, "Passed")



    def testAddItem(self):
        out = self.handleInputs.addItem(
            inputs={

                "itemName": "DummyItem",
                "cost": 500,
                "subtype": "Electronics",
                "replacementDuration": 1,
                "dateCreated": "2021-01-01",
                "dateOfReplacement": "2022-01-02",
            }
        )
        # self.delete.deleteData(value="DummyItem")

        self.assertEqual(out, 0, "Passed")
        
    # def testDisplay(self):
    #     self.assertEqual(Display.display(), Constants.EXIT_CODE.SUCCESS.value, "Passed")    

    # def testInputPassedAsArgument(self):
    #     out = self.handleInputs.addItem(
    #         inputs={
    #             "itemName": "TestInput",
    #             "cost": 100,
    #             "subtype": "TestSubtype",
    #             "replacementDuration": 10,
    #             "dateCreated": "2021-01-01",
    #             "dateOfReplacement": "2022-01-02",
    #         }
    #     )

    #     if out == 0:
    #         out = self.delete.deleteData(value="1000")
    #         if out != 0:
    #             self.assertNotEqual(out, 0, "Passed")
    #     else:
    #         self.assertNotEqual(out, 0, "Passed")
    #     self.assertEqual(out, 0, "Passed")

    def testExport2CSV(self):
        self.assertEqual(
            Export2CSV.export2CSV(), Constants.EXIT_CODE.SUCCESS.value, "Passed"
        )



    # Tests for inputValidation
    def testValidateInput(self):
        test = {"key": "itemName", "value": "TestInput"}
        self.assertEqual(
            Validation.validateInput(test), Constants.EXIT_CODE.SUCCESS.value, "Passed"
        )

    def testValidateInputCost(self):
        test = {"key": "cost", "value": "1"}
        self.assertEqual(
            Validation.validateInput(test), Constants.EXIT_CODE.SUCCESS.value, "Passed"
        )

    def testValidateInputCostFail(self):
        test = {"key": "cost", "value": "xyz"}
        self.assertEqual(
            Validation.validateInput(test), Constants.EXIT_CODE.INVALID.value, "Passed"
        )

    def testValidateInputDuration(self):
        test = {"key": "replacementDuration", "value": "1"}
        self.assertEqual(
            Validation.validateInput(test), Constants.EXIT_CODE.SUCCESS.value, "Passed"
        )

    def testValidateInputDurationFail(self):
        test = {"key": "replacementDuration", "value": "xyz"}
        self.assertEqual(
            Validation.validateInput(test), Constants.EXIT_CODE.INVALID.value, "Passed"
        )

    def testValidateInputFail2(self):
        test = {"key": "subtype", "value": "sa"}
        self.assertEqual(
            Validation.validateInput(test), Constants.EXIT_CODE.SUCCESS.value, "Passed"
        )

    def testEditInventory(self):
        
        inputs = {
            "item_name": "edited_item",
            "cost": "99",
            "subtype": "household",
            "replacement_duration": 2,
            "dateCreated": "2024-01-01",
            "dateOfReplacement": "2024-03-01",
        }
        out=self.edit.editItem(1, inputs)
        self.assertEqual(out,Constants.EXIT_CODE.SUCCESS.value)

if __name__ == "__main__":
    unittest.main()
