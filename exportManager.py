import sqlite3
import Constants


class ReadFromCSV:
    def readFromCSV():
        df = pd.read_csv(Constants.CSV_FILE)
        print(df)
        return


class Export2CSV:
    def export2CSV():
        try:
            conn = sqlite3.connect(Constants.DB_FILE)
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
