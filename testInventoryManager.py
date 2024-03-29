import unittest
from inventoryManager import Menu, HandleInputs,Display, Search, Delete
from exportManager import Export2CSV
import Constants

class TestInventoryManager(unittest.TestCase):
    
    menu = Menu()
    handleInputs = HandleInputs()
    export2csv = Export2CSV()
    display = Display()
    delete = Delete()
    
    def testExitOutOfMenu(self):
        out=self.menu.handleMenu(choice=Constants.ACTION.EXIT.value);
        self.assertEqual(out,0,"Passed");
        
    # def testFailExitOutOfMenu(self):
    #     out=self.inventory_manager.handleMenu(choice='7');
    #     self.assertNotEqual(out,0,"Passed");
        
        
    def testInputPassedAsArgument(self):
        out=self.handleInputs.handleInputs(inputs={'itemName':'TestInput','cost':100,'subtype':'TestSubtype','replacementDuration':10});
        self.assertEqual(out,0,"Passed");
    
    # def testInputWithSpecialCharactersInput(self):
    #     return NotImplementedError
    
    def testExport2CSV(self):
        self.assertEqual(Export2CSV.export2CSV(),Constants.EXIT_CODE.SUCCESS.value,"Passed");
    
    def testDisplay(self):
        self.assertEqual(Display.display(),Constants.EXIT_CODE.SUCCESS.value,"Passed");
        
    # def testSearch(self):
    #     self.assertEqual(Search.search(),Constants.EXIT_CODE.SUCCESS.value,"Passed");
    
    # def testDelete(self):
    #     self.assertEqual(Delete.deleteData(),Constants.EXIT_CODE.SUCCESS.value,"Passed");
    
    '''Todo :
    # 1. ValidationForInput  - Empty, Long, Junk Characters.
    # 2. testMethodForInputs, exporting to CSV, Printing!
    '''
if __name__ == '__main__':
    unittest.main()
    
