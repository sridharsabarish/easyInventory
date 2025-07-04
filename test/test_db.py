import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from classes.Item import Item
from classes.DB import DB

class TestDataBase:
    @pytest.fixture(autouse=True)
    def test_create_db(self):
        
        try:
            DB.createTable("test.db")
            #os.remove("test.db")
            assert True
        except Exception as e:
            assert False, f"An error occurred: {e}"
        finally:
            os.remove("test.db")


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