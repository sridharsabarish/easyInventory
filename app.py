from flask import Flask, render_template, request
from inventoryManager import Add, Fetch, Delete, Search
import csv
from flask import send_file

app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        # Handle form submission and update inventory
        item_name = request.form.get('item_name')
        quantity = request.form.get('quantity')
        # Add your logic to update the inventory here

    # Render the inventory template
    return render_template('inventory.html')

@app.route('/inventory/add', methods=['GET', 'POST'])
def add():
    
    add = Add()
    if request.method == 'POST':
        # Handle form submission and add new item to inventory
        item_name = request.form.get('name')
        cost = request.form.get('cost')
        subtype = request.form.get('subtype')
        replacement_duration = request.form.get('replacementDuration')
        
        # Create a new item object
        inputs = {
            'item_name': item_name,
            'cost': cost,
            'subtype': subtype,
            'replacement_duration': replacement_duration
        }
        
       
        # Add the new item to the inventory
        # Add your logic to add the item to the inventory here
        print(inputs)
        add.addItem(inputs)
        

    # Render the add template
    return render_template('add.html')

@app.route('/inventory/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        # Handle form submission and delete item from inventory
        item_name = request.form.get('item_name')
        # Add your logic to delete the item from the inventory here

    # Redirect to the inventory page after deletion
    return redirect('/inventory')

@app.route('/inventory/display')
def display():
    # Add your logic to retrieve and display the inventory here
    display = Fetch()
    info_for_html = display.fetchAllInfo()
    print(info_for_html)
    return render_template('display.html', inventory=info_for_html)
    
    
    # Render the display template
    return render_template('display.html')

@app.route('/inventory/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        # Handle form submission and search for items in inventory
        search_query = request.form.get('search_query')
        # Add your logic to search for items in the inventory here

    # Render the search template
    return render_template('search.html')

@app.route('/inventory/download', methods=['GET'])
def download():
    # Add your logic to generate and download the CSV file here
    # For example, you can use the csv module to create the file
    inventory = Fetch().fetchAllInfo()
    filename = 'inventory.csv'  # Replace with the desired file path
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item Name', 'Cost', 'Subtype', 'Replacement Duration'])
        for item in inventory:
            writer.writerow([item['name'], item['cost'], item['subtype'], item['replacementDuration']])
    return send_file(filename, as_attachment=True)    


if __name__ == '__main__':
    app.run(debug=True)