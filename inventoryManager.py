from Item import Item
from exportManager import exportManager
import Constants, Beautify, re, sqlite3
from collections import defaultdict
import tkinter as tk

def saveToDB(item):
    conn = sqlite3.connect(Constants.DB_FILE)
    cursor = conn.cursor()
    # Create the table if it doesn't exist
    cursor.execute(Constants.CREATE_TABLE)
    # Save the variables to the database
    cursor.execute(Constants.INSERT_TO_DB, (item.getItemName(), item.getCost(), item.getSubtype(), item.getReplacementDuration()))
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

    def handleInputs(self,inputs={}):

        # Todo : Connect this to a GUI
        # Todo get the columns using the data types supported by the item.py class automatically.
        val ={};
        
        print(len(inputs))
        if len(inputs)!=4:
            for i in range(0,len(Constants.ITEM_SCHEMA)):
                x=self.readInput(Constants.ITEM_SCHEMA[i]);
                val[i]=x;
        else:
            # Todo : validate output
            val=inputs;
        
        newItem = Item(*val.values())
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
        name=input(Constants.DELETE_PRODUCT_PROMPT)
        conn = sqlite3.connect(Constants.DB_FILE)
        cursor = conn.cursor()
        
        # Check if the item exists
        cursor.execute(Constants.SEARCH_QUERY, (name,))
        if cursor.fetchone() is None:
            print(Constants.ERROR_PRODUCT)
            
        else:
            print(Constants.SUCCESS_PRODUCT)
            self.display();
        
            cursor.execute(Constants.DELETE_ITEM_QUERY, (name,))
            
            
        conn.commit()
        conn.close()
        print(Constants.DELETED_PRODUCT);
        exportManager.export2CSV()
        return
    
    # Todo : Refactor/Refine search further
    def search(self):
        gui = GUI()
        gui.search()
        ~gui
        return 
        
    def handleMenu(self,choice=''):
        # Todo : Check if it is possible to replace function call with Dictionary
            function_dict = {
                Constants.ACTION.DISPLAY.value: self.display,
                Constants.ACTION.EXPORT_CSV.value: exportManager.export2CSV,
                Constants.ACTION.DELETE.value: self.deleteData,
                Constants.ACTION.READ_CSV.value: exportManager.readFromCSV,
                Constants.ACTION.SEARCH.value: self.search
            }

            while True:
                if choice == '':
                    choice = input(Constants.menuString)
                    print(choice)
                elif choice==  Constants.ACTION.INSERT.value:
                    self.handleInputs(inputs={});
                    choice = ''
                    continue
                elif choice in function_dict:
                    function_dict[choice]()
                    choice = ''
                    continue
                else:
                    if(choice==Constants.ACTION.EXIT.value):
                        return(Constants.EXIT_CODE.EXIT.value)
                    print(Constants.INVALID_CHOICE)
                    return Constants.EXIT_CODE.INVALID_CHOICE.value

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Inventory Search")
        
        self.label = tk.Label(self.window, text="Enter the name of the product to be searched:")
        self.label.pack()
        
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        
        self.button = tk.Button(self.window, text="Search", command=self.search)
        self.button.pack()
        
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
        
        self.table = tk.Text(self.window)
        self.table.pack()
        
        self.exit_button = tk.Button(self.window, text="Exit", command=self.window.destroy)
        self.exit_button.pack(side=tk.BOTTOM)
        
        self.window.mainloop()
    
    def search(self):
        product_name = self.entry.get()
        conn = sqlite3.connect(Constants.DB_FILE)
        cursor = conn.cursor()
        rows = cursor.execute(Constants.SEARCH_QUERY, (product_name,))
        results = cursor.fetchall()
        conn.close()
        self.result_label.config(text="Search Result:")
        self.table.delete(1.0, tk.END)
        self.table.insert(tk.END, "{:<20} {:<10} {:<15} {:<20}\n".format("Item Name", "Cost", "Subtype", "Replacement Duration"))
        self.table.insert(tk.END, "-" * 70 + "\n")
        
        for result in results:
            self.table.insert(tk.END, "{:<20} {:<10} {:<15} {:<20}\n".format(result[0], result[1], result[2], result[3]))
            self.table.insert(tk.END, "\n")




if __name__ == '__main__':
    inventory_manager = InventoryManager()
    export_manager = exportManager()
    inventory_manager.handleMenu(choice='');
    
    
'''
Todo : Setup a jenkins Job using RPI as a slave
Todo : Fix input bug
Todo : Make GUI Inputs.
Todo : Add protection against Dependency Injection Attacks. 
Todo : Rethink Schema for the GUI
'''