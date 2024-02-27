import sqlite3
from Item import Item
from exportManager import exportManager
import Constants
import Beautify
import re
from collections import defaultdict

def saveToDB(newItem):
    conn = sqlite3.connect(Constants.DB_FILE)
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute(Constants.CREATE_TABLE)
    # Save the variables to the database
    cursor.execute(Constants.INSERT_TO_DB, (newItem.getItemName(), newItem.getCost(), newItem.getSubtype(), newItem.getReplacementDuration()))

    # Commit the changes and close the connection
    conn.commit()
    conn.close() 


class InventoryManager:
    def readInput(self,x) -> str: 
        match =False
        pattern = re.compile(Constants.regex_map[x])
        while match is False:
            output = input(x+": ");
            match = bool(pattern.match(output))
        return output

    def handleInputs(self,inputs):

        # Todo : Connect this to a GUI
        lists =["itemName","subtype","cost","replacementDuration"];
        val ={};
        
        if len(inputs)!=4:
            for i in range(0,len(lists)):
                x=self.readInput(lists[i]);
                val[lists[i]]=x;
        else:
            val=inputs;
        
        newItem = Item(val["itemName"],val["cost"],val["subtype"],val["replacementDuration"]);
        # Connect to the database
        saveToDB(newItem)
        exportManager.export2CSV()
        return 0;
        
        
    def display(self):
        conn = sqlite3.connect(Constants.DB_FILE)
        cursor = conn.cursor()

        # Select all of the items from the database
        cursor.execute(Constants.SELECT_ALL)
        # Initialize variables for most expensive item and shortest replacement duration
        most_expensive_item = None
        shortest_replacement_duration = None
        
        
        
        counts=defaultdict(int); # Keep count of all the items
        # Print the items
        total_cost = 0
        for row in cursor.fetchall():
            print(row)
            total_cost += row[1]  # Assuming cost is stored in the second column
            
            counts[row[0].lower()]+=1;
            # Check if the current item is the most expensive
            if most_expensive_item is None or row[1] > most_expensive_item[1]:
                most_expensive_item = row
            # Check if the current item has the shortest replacement duration
            if shortest_replacement_duration is None or row[3] < shortest_replacement_duration[3]:
                shortest_replacement_duration = row
        
        
        
        for i in counts.keys():
            print(f'{i}:{counts[i]}');
        
        Beautify.lineBreak()
        print("Total cost: ${:.2f}".format(total_cost))
        print("Most expensive item: {}".format(most_expensive_item[0]))
        print("Item with shortest replacement duration: {}".format(shortest_replacement_duration[0]))
        Beautify.lineBreak()
        
        # Close the connection
        conn.close()
        return total_cost
    def deleteData(self):
        #Todo  : Remove a product from the inventory
        name=input("Enter the name of the product to be deleted: ")
        conn = sqlite3.connect(Constants.DB_FILE)
        cursor = conn.cursor()
        
        # Check if the item exists
        cursor.execute('''
            SELECT * FROM inventory WHERE item_name = ?
        ''', (name,))
        if cursor.fetchone() is None:
            print('Product not found')
            
            print("These are the products available")
            self.display();
            return
        
        cursor.execute('''
            DELETE FROM inventory WHERE item_name = ?
        ''', (name,))
        conn.commit()
        conn.close()
        print('Product deleted')
        exportManager.export2CSV()
        return
    
    def handleMenu(self,choice=''):
        while True:
            
            
            if choice=='':
                choice = input("MENU \n 1. Add an item \n 2 Display the items \n 3.Export to CSV \n 4.Delete item \n 5. Read from CSV \n 6. Exit \n Enter your choice: ")
            # Todo : Get the user input from a GUI
            if choice == '1':
                inventory_manager.handleInputs(inputs={})
                choice=''
                continue
            if choice == '2':
                inventory_manager.display()
                choice=''
                continue
            if(choice =='3'):
                exportManager.export2CSV();
                choice=''
                continue
            if(choice =='4'):
                inventory_manager.deleteData();
                choice=''
                continue
            if(choice =='5'):
                exportManager.readFromCSV();
                choice=''
                continue
            if(choice=='6'):
                return 0;
            else:
                print("Invalid choice, Terminating")
                return -1;
    
if __name__ == '__main__':
    
    inventory_manager = InventoryManager()
    export_manager = exportManager()
    inventory_manager.handleMenu(choice='');
    

'''
Todo : Add a GUI - Make a web ap using Flask

* Use Dictionaries to populate items and keep count
Todo : Fix the logic of menu to avoid breaking out.
Todo : Add protection against Dependency Injection Attacks.
'''