
import sys
import os
import pytest 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from classes.Item import Item

@pytest.fixture
def default_item():
    item = Item("D","300","200","12",12,21)
    return item

class TestItem:




    def test_incorrect_item(self):
        try:
            item = Item("D","300","200","12",12,21,21)
            assert False

        except TypeError as e:
            #assert str(e) == "__init__() takes 6 arguments (7 given)"
            assert True
        
        
    def test_item(self):
        try:
            item = Item("DummyThing",200,"Clothing",12,"2023-01-01",12)
        except Exception as e:
            assert False
        assert True

    def test_get_item_getCost(self,default_item):
        try:
            cost =default_item.getCost()
        except:
            assert False
        finally:
            assert True

    def test_get_item_getCost(self,default_item):
        try:
            cost =default_item.getCost()
        except:
            assert False
        finally:
            assert True

    def test_get_item_getSubtype(self,default_item):
        try:
            cost =default_item.getSubtype()
        except:
            assert False
        finally:
            assert True

    def test_get_item_getDateCreated(self,default_item):
        try:
            cost =default_item.getDateCreated()
        except:
            assert False
        finally:
            assert True
    def test_get_item_getDateOfReplacement(self,default_item):
        try:
            cost =default_item.getDateOfReplacement()
        except:
            assert False
        finally:
            assert True