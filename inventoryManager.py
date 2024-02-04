import sqlite3


        
validateString = lambda x: x.isalpha() or x.isdigit() and x!=''
validateNumber = lambda x: x.isdigit() and x!=''
validateFloat = lambda x: x.isdigit() and x!=''


def saveToDB(newItem):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            item_name TEXT,
            cost REAL,
            subtype TEXT,
            replacement_duration INTEGER
        )
    ''')
    # Save the variables to the database
    cursor.execute('''
        INSERT INTO inventory (item_name, cost, subtype, replacement_duration)
        VALUES (?, ?, ?, ?)
    ''', (newItem.getItemName(), newItem.getCost(), newItem.getSubtype(), newItem.getReplacementDuration()))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
def readInput(x) -> str: 
    output = input(x+": ");
    # Todo : modify the validation below according to the data type.
    while( not validateString(output) ):
        print(" Enter a valid ",output)
        output = input(x,": ")    
    return output

def lineSeperator():
    print("--------------------------------------------------")
    
class Item:
    
    def __init__(self, name, cost, subtype, replacementDuration):
        self.itemName = name
        self.cost = cost
        self.subtype = subtype
        self.replacementDuration = replacementDuration
    def getItemName(self):
        return self.itemName
    def getCost(self):
        return self.cost
    def getSubtype(self):
        return self.subtype
    def getReplacementDuration(self):
        return self.replacementDuration

class InventoryManager:
    def takeInputs(self):
        # Todo : Write Tests that would break these inputs.
        validateString = lambda x: x.isalpha() or x.isdigit() and x!=''
        validateNumber = lambda x: x.isdigit() and x!=''
        validateFloat = lambda x: x.isdigit() and x!=''

        # Todo : Connect this to a GUI
        lists =["itemName","subtype","cost","replacementDuration"];
        val ={};
        for i in range(0,len(lists)):
            x=readInput(lists[i]);
            val[lists[i]]=x;
        
        newItem = Item(val["itemName"],val["cost"],val["subtype"],val["replacementDuration"]);
        # Connect to the database
        saveToDB(newItem)
        export2CSV()
        
        
    def display(self):
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()

        # Select all of the items from the database
        cursor.execute('''
            SELECT * FROM inventory
        ''')
        # Initialize variables for most expensive item and shortest replacement duration
        most_expensive_item = None
        shortest_replacement_duration = None
        # Print the items
        total_cost = 0
        for row in cursor.fetchall():
            print(row)
            total_cost += row[1]  # Assuming cost is stored in the second column

            # Check if the current item is the most expensive
            if most_expensive_item is None or row[1] > most_expensive_item[1]:
                most_expensive_item = row
            # Check if the current item has the shortest replacement duration
            if shortest_replacement_duration is None or row[3] < shortest_replacement_duration[3]:
                shortest_replacement_duration = row
        
        lineSeperator()
        print("Total cost: ${:.2f}".format(total_cost))
        print("Most expensive item: {}".format(most_expensive_item[0]))
        print("Item with shortest replacement duration: {}".format(shortest_replacement_duration[0]))
        lineSeperator()
        
        # Close the connection
        conn.close()
        return total_cost
    def deleteData(self):
        #Todo  : Remove a product from the inventory
        name=input("Enter the name of the product to be deleted: ")
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        
        # Check if the item exists
        cursor.execute('''
            SELECT * FROM inventory WHERE item_name = ?
        ''', (name,))
        if cursor.fetchone() is None:
            print('Product not found')
            return
        
        cursor.execute('''
            DELETE FROM inventory WHERE item_name = ?
        ''', (name,))
        conn.commit()
        conn.close()
        print('Product deleted')
        export2CSV()
        return
'''

Todo : Read from CSV Feature
Todo : Add a GUI
Todo : Read from CSV and update the db
and do a data analysis on the data
'''

def readFromCSV():
    #Todo
    return


def guiInput():
    #Todo
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

if __name__ == '__main__':
    inventory_manager = InventoryManager()
    ch = 'y'
    while ch == 'y':
        choice = input("MENU \n 1. Add an item \n 2 Display the items \n 3.Export to CSV \n 4.Delete item \n Enter your choice: ")
        # Todo : Get the user input from a GUI
        if choice == '1':
            inventory_manager.takeInputs()
        if choice == '2':
            inventory_manager.display()
        if(choice =='3'):
            export2CSV();
        if(choice =='4'):
            inventory_manager.deleteData();
            
        ch = input("Do you want to continue y/n ")
