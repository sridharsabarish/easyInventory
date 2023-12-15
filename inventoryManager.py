import sqlite3
# Need to figure out a way to use the db
# Need a good UI for taking inputs.

validateString = lambda x: x.isalpha() or x.isdigit() and x!=''
validateNumber = lambda x: x.isdigit() and x!=''
validateFloat = lambda x: x.isdigit() and x!=''

def takeInputs():
    
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

def display():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Select all of the items from the database
    cursor.execute('''
        SELECT * FROM inventory
    ''')

    # Print the items
    total_cost = 0
    for row in cursor.fetchall():
        print(row)
        total_cost += row[1]  # Assuming cost is stored in the second column

    print("Total cost:", total_cost)

    # Close the connection
    conn.close()

    return total_cost


if __name__ == '__main__':
    
    ch ='y'
    while(ch=='y'):
        choice = input("Enter 1 to add an item, 2 to display the items ")
        if choice == '1':
            takeInputs()
        if choice == '2':
            display()
        ch=input("Do you want to continue y/n ")