from flask import Flask, render_template, request
from inventoryManager import Add, Fetch, Delete, Search, DB
import csv
from flask import send_file
import Constants
import sqlite3

app = Flask(__name__)


# Define routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    if request.method == "POST":
        # Handle form submission and update inventory
        item_name = request.form.get("item_name")
        quantity = request.form.get("quantity")
        # Add your logic to update the inventory here

    # Render the inventory template
    return render_template("inventory.html")


@app.route("/inventory/add", methods=["GET", "POST"])
def add():

    add = Add()
    if request.method == "POST":
        # Handle form submission and add new item to inventory
        item_name = request.form.get("name")
        cost = request.form.get("cost")
        subtype = request.form.get("subtype")
        if subtype not in Constants.ALLOWED_SUBTYPES:
            # Handle invalid subtype value here
            # For example, you can display an error message or redirect to an error page
            return render_template("error.html", message="Invalid subtype value")
        replacement_duration = request.form.get("replacementDuration")

        # Create a new item object
        inputs = {
            "item_name": item_name,
            "cost": cost,
            "subtype": subtype,
            "replacement_duration": replacement_duration,
        }

        # Add the new item to the inventory
        # Add your logic to add the item to the inventory here
        print(inputs)
        add.addItem(inputs)

    # Render the add template
    return render_template("add.html")


@app.route("/inventory/delete", methods=["GET", "POST"])
def delete(productName=None):

    delete = Delete()
    print(productName)

    if request.method == "POST":
        item_name = request.form.get("name")
        print("The product name is ", item_name)
        delete.deleteData(str(item_name))

        # Handle form submission and delete item from inventory
        # Add your logic to delete the item from the inventory here
    # Redirect to the inventory page after deletion
    return render_template("delete.html")


@app.route("/inventory/display")
def display():
    # Add your logic to retrieve and display the inventory here
    display = Fetch()
    info_for_html = display.fetchAllInfo()
    print(info_for_html)
    return render_template("display.html", inventory=info_for_html)


@app.route("/inventory/search", methods=["GET", "POST"])
def search():
    if request.method =="POST":
        # Handle form submission and search for items in inventory
        search_query = request.form.get("search_query")
        print("The search query is ", search_query)
        fetch = Fetch()
        info_for_html = fetch.fetchInfo(search_query)
        if(info_for_html!=[]):
            print(info_for_html)        
            return render_template("display.html", inventory=info_for_html)
        
        # Add your logic to search for items in the inventory here
        # Assuming you have a function called searchItems() that returns the result of the SQL query
        # Display the search result


    # Render the search template
    return render_template("search.html")


@app.route("/inventory/download", methods=["GET"])
def download():
    # Add your logic to generate and download the CSV file here
    # For example, you can use the csv module to create the file
    inventory = Fetch().fetchAllInfo()
    filename = "inventory.csv"  # Replace with the desired file path
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item Name", "Cost", "Subtype", "Replacement Duration"])
        for item in inventory:
            writer.writerow(
                [
                    item["name"],
                    item["cost"],
                    item["subtype"],
                    item["replacementDuration"],
                ]
            )
    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host='192.168.0.101', port=3000, debug=True)
