import unittest
from InventoryManager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    
    inventory_manager = InventoryManager()
    
    def testExitOutOfMenu(self):
        out=self.inventory_manager.handleMenu(choice='6');
        self.assertEqual(out,0,"Passed");
        
    def testFailExitOutOfMenu(self):
        out=self.inventory_manager.handleMenu(choice='7');
        self.assertNotEqual(out,0,"Passed");
        
        
    def testInputPassedAsArgument(self):
        out=self.inventory_manager.handleInputs(inputs={'itemName':'TestInput','subtype':'TestSubtype','cost':100,'replacementDuration':10});
        self.assertEqual(out,0,"Passed");
    
    def testInputWithSpecialCharactersInput(self):
        return NotImplementedError
    
    def testExportToCSVFunctionality(self):
        return NotImplementedError
    
    def testPrintFunctionality(self):
        return NotImplementedError
        
    
    '''Todo :
    # 1. ValidationForInput  - Empty, Long, Junk Characters.
    # 2. testMethodForInputs, exporting to CSV, Printing!
    '''
if __name__ == '__main__':
    unittest.main()
    
