import sqlite3
import static.Constants as Constants
import os


class Export2CSV:
    def export2CSV(DBFILE=Constants.DB_FILE):
        try:
            
            conn = sqlite3.connect(DBFILE)
            
            if not os.path.exists(DBFILE):
                return -1
            cursor = conn.cursor()
            cursor.execute(Constants.SELECT_ALL)
            with open(Constants.CSV_FILE, "w") as file:
                for row in cursor.fetchall():
                    file.write(",".join(str(x) for x in row) + "\n")
            conn.close()
            print(f"Data exported to {Constants.CSV_FILE}")
            return 0
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return -1
