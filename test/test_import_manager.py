import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from classes.import_manager import import_manager
def test_import_manager():
    try:
        importManager = import_manager()
        assert True
    except:
        assert False
        
@pytest.mark.skip        
def test_import_csv_object():
    try:
        importManager = import_manager()
        importManager.import_csv(CSV_FILE='inventory.csv')
        assert True
    except:
        assert False    
        

@pytest.mark.skip        
def test_import_csv_persist_to_db():
    assert False