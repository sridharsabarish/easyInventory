import unittest
from inventoryManager import Menu, Add, Display, Delete, Validation, DB
from exportManager import Export2CSV
import Constants


class TestInventoryManager(unittest.TestCase):

    menu = Menu()
    handleInputs = Add()
    export2csv = Export2CSV()
    display = Display()
    delete = Delete()

    def testCreateEmptyDB(self):
        out = DB.createTable()
        self.assertEqual(out, Constants.EXIT_CODE.SUCCESS.value, "Passed")

    def testExitOutOfMenu(self):
        out = self.menu.handleMenu(choice=Constants.ACTION.EXIT.value)
        self.assertEqual(out, 0, "Passed")

    def testAddItem(self):
        out = self.handleInputs.addItem(
            inputs={
                "itemName": "DummyItem",
                "cost": 500,
                "subtype": "Electronics",
                "replacementDuration": 1,
            }
        )
        self.delete.deleteData(value="DummyItem")

        self.assertEqual(out, 0, "Passed")

    def testInputPassedAsArgument(self):
        out = self.handleInputs.addItem(
            inputs={
                "itemName": "TestInput",
                "cost": 100,
                "subtype": "TestSubtype",
                "replacementDuration": 10,
            }
        )

        if out == 0:
            out = self.delete.deleteData(value="TestInput")
            if out != 0:
                self.assertNotEqual(out, 0, "Passed")
        else:
            self.assertNotEqual(out, 0, "Passed")
        self.assertEqual(out, 0, "Passed")

    def testExport2CSV(self):
        self.assertEqual(
            Export2CSV.export2CSV(), Constants.EXIT_CODE.SUCCESS.value, "Passed"
        )

    def testDisplay(self):
        self.assertEqual(Display.display(), Constants.EXIT_CODE.SUCCESS.value, "Passed")

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

    # def testDeleteTestInput(self):
    #      name = 'TestInput'

    #      print("came here")
    #      out = Delete.deleteData(name)
    #      print("Here too")
    #      self.assertNotEqual(out,Constants.EXIT_CODE.SUCCESS.value,"Passed");

    # def testSearch(self):
    #     self.assertEqual(Search.search(),Constants.EXIT_CODE.SUCCESS.value,"Passed");

    # def testDelete(self):
    #     self.assertEqual(Delete.deleteData(),Constants.EXIT_CODE.SUCCESS.value,"Passed");


if __name__ == "__main__":
    unittest.main()
