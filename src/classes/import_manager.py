import sqlite3
import static.Constants as Constants
import os
import csv
class import_manager:
    def __init__(self):
        pass
    
    def import_csv(self,CSV_FILE,DB_FILE=Constants.DB_FILE):
        
        
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row.
            for row in reader:
                c.execute("INSERT INTO inventory VALUES (?,?,?,?,?,?,?)", row)
                

        conn.commit()
        conn.close()
