import unittest
from InventoryManager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    
    inventory_manager = InventoryManager()
    
    def testExitOutOfMenu(self):
        out=self.inventory_manager.handleMenu(choice='6');
        self.assertEquals(out,0,"Passed");
        
    def testFailExitOutOfMenu(self):
        out=self.inventory_manager.handleMenu(choice='7');
        self.assertNotEquals(out,0,"Passed");
        
    
    '''Todo :
    # 1. ValidationForInput  - Empty, Long, Junk Characters.
    # 2. testMethodForInputs, exporting to CSV, Printing!
    '''
if __name__ == '__main__':
    unittest.main()
    
