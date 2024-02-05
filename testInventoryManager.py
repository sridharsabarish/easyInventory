import unittest
from InventoryManager import InventoryManager

class TestInventoryManager(unittest.TestCase):
    def testExitOutOfMenu(self):
        out=InventoryManager.handleMenu(6);
        self.assertEqual(out,0,"Passed");
    
if __name__ == '__main__':
    unittest.main()
    
