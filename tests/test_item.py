
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from classes.Item import Item




def test_incorrect_item():
    try:
        item = Item("D","300","200","12",12,21,21)
        assert False

    except TypeError as e:
        #assert str(e) == "__init__() takes 6 arguments (7 given)"
        assert True
    
    
def test_item():
    try:
        item = Item("DummyThing",200,"Clothing",12,"2023-01-01",12)
    except Exception as e:
        assert False
    assert True