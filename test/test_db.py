import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from classes.Item import Item
from classes.DB import DB


class TestPrerequisites:
    def test_connect_to_db(self):
        dbObj = DB()
        try:
            dbObj.connect()
        except:
            assert False
        finally:
            assert True


class TestDataBase:
    @pytest.fixture(autouse=True)
    def test_create_db(self):
        
        try:
            out=DB.createTable(DBFILE="test.db")
            
            #os.remove("test.db")
            assert out is not True
        except Exception as e:
            assert False, f"An error occurred: {e}"

    def test_fail_create_existing_db(self):
        
        try:
            out = DB.createTable(DBFILE="inventory.db")
            assert out is False
            #os.remove("test.db")
            assert True
        except Exception as e:
            assert False, f"An error occurred: {e}"


    def test_save_item_to_db(self):
        try:
            item = Item("DummyThing",200,"Clothing",12,"2023-01-01",12)
            DB.saveToDB(item,"test.db")
            
            assert True
        except Exception as e:
            assert False, f"An error occurred: {e}"
            
    def test_delete_db(self):
        try:
            os.remove("test.db")
            assert True
        except Exception as e:
            assert False, f"An error occurred: {e}"


    def test_edit_db(self):
        #TODO : Make changes
        assert True