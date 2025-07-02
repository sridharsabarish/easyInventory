import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from classes.exportManager import Export2CSV
def test_create_export_manager_object():
    
    try:
        export2csv = Export2CSV()
        assert True
    except Exception as e:
        assert False, f"An error occurred: {e}"
        
        
def test_exporting_a_file_incorrect():
    try:
        out =Export2CSV.export2CSV(DBFILE="tes2t.db")
        if(out==0):
            assert False
        assert True
    except Exception as e:
        assert False, f"An error occurred: {e}"
        
        
def test_exporting_a_file_correct():
    try:
        out =Export2CSV.export2CSV()
        if(out!=0):
            assert False
        assert True
    except Exception as e:
        assert False, f"An error occurred: {e}"