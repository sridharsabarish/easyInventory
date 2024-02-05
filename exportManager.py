import sqlite3
import pandas as pd
class exportManager:
    
    def readFromCSV():
        #Todo
        
        df =pd.read_csv('inventory.csv')
        print(df.head())
        return

    def export2CSV():
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM inventory
        ''')
        with open('inventory.csv', 'w') as file:
            for row in cursor.fetchall():
                file.write(','.join(str(x) for x in row) + '\n')
        conn.close()
        print('Data exported to inventory.csv')