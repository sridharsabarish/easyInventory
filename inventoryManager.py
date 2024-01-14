import sqlite3
class InventoryManager:
    def takeInputs(self):
        
        validateString = lambda x: x.isalpha() or x.isdigit() and x!=''
        validateNumber = lambda x: x.isdigit() and x!=''
        validateFloat = lambda x: x.isdigit() and x!=''
        
        itemName = input("Enter the Item ")
        while( not validateString(itemName) ):
            print(" Enter a valid item name ")
            itemName = input("Enter the Item ")
                
        cost = input("Cost ")
        
        while( not validateFloat(cost) ):
            print(" Enter a valid cost ")
            cost = input("Cost ")
            
        subtype=input("SubType ")
        while( not validateString(subtype) ):
            print(" Enter a valid subtype ")
            subtype=input("SubType ")
        
        replacementDuration=input("Replacement Duration ")
        while( not validateNumber(replacementDuration) ):
            print(" Enter a valid replacement duration ")
            replacementDuration=input("Replacement Duration ")
            
            # Connect to the database
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
        ''', (itemName, cost, subtype, replacementDuration))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
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
        print("--------------------")  # Add a line separator
        print("Total cost: ${:.2f}".format(total_cost))
        print("Most expensive item: {}".format(most_expensive_item[0]))
        print("Item with shortest replacement duration: {}".format(shortest_replacement_duration[0]))

        print("--------------------")  # Add a line separator
        # Close the connection
        conn.close()
        return total_cost

if __name__ == '__main__':
    inventory_manager = InventoryManager()
    ch = 'y'
    while ch == 'y':
        choice = input("Enter 1 to add an item, 2 to display the items ")
        if choice == '1':
            inventory_manager.takeInputs()
        if choice == '2':
            inventory_manager.display()
        ch = input("Do you want to continue y/n ")
