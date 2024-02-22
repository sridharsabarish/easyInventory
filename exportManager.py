import sqlite3
import pandas as pd
import Constants
class exportManager:
    def readFromCSV():
        df =pd.read_csv(Constants.CSV_FILE)
        print(df.head())
        return

    def export2CSV():
        conn = sqlite3.connect(Constants.DB_FILE)
        cursor = conn.cursor()
        cursor.execute(Constants.SELECT_ALL)
        with open(Constants.CSV_FILE, 'w') as file:
            for row in cursor.fetchall():
                file.write(','.join(str(x) for x in row) + '\n')
        conn.close()
        print('Data exported to inventory.csv')