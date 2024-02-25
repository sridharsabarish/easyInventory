from InventoryManager import InventoryManager
inventory_manager = InventoryManager()


def test_correct_exit():
    assert inventory_manager.handleMenu(choice='6')==0;

def test_incorrect_exit():
    assert inventory_manager.handleMenu(choice='7')!=0;
    
def testInputWithSpecialCharactersInput():
    assert False
    
def testExportToCSVFunctionality():
    assert False
    
def testPrintFunctionality():
    assert False
    

'''Todo :
# 1. ValidationForInput  - Empty, Long, Junk Characters.
# 2. testMethodForInputs, exporting to CSV, Printing!
'''