
from loguru import logger
log_path = "out/logs/"
logger.add(log_path+"app.log", rotation="1 week", retention="1 month", level="DEBUG")

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
logger.debug(sys.path)
from flask import Flask, render_template, request, redirect
from src.classes.inventoryManager import Add, Fetch, Delete, DB, Edit
logger.debug("Added classes")
import csv
from flask import send_file

import src.static.Constants as Constants
logger.debug("Added constants")
import sqlite3
import datetime
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

import loguru
# Set up logging
logger2 = loguru.logger
logger2.add(log_path+"debugLogs.log", format="{time} {level} {message}", level="DEBUG", serialize=True)
logger.debug("Logger initialized")
# Define routes
@app.route("/")
def home():
    logger.debug("Rendering Home page")
    return render_template(Constants.INDEX_PAGE)
    logger.debug("Home page")


@app.route("/inventory", methods=["GET", "POST"])
def inventory():
    if request.method == "POST":
        item_name = request.form.get("item_name")
        quantity = request.form.get("quantity")
    return render_template(Constants.INVENTORY_PAGE)


@app.route("/inventory/add", methods=["GET", "POST"])
def add():

    add = Add()
    if request.method == "POST":
        # Handle form submission and add new item to inventory
        item_name = request.form.get("name")
        cost = request.form.get("cost")
        subtype = request.form.get("subtype")
        dateCreated = request.form.get("dateCreated")
        dateCreated_date = datetime.datetime.strptime(dateCreated, "%Y-%m-%d").date()
        dateOfReplacement = dateCreated_date + (datetime.timedelta(days=int(request.form.get("replacementDuration")))*31)     
        if subtype not in Constants.ALLOWED_SUBTYPES:
            # Handle invalid subtype value here
            # For example, you can display an error message or redirect to an error page
            logger.error("Invalid subtype value")
            return render_template(Constants.ERROR_PAGE, message="Invalid subtype value")
        replacement_duration = request.form.get("replacementDuration")

        # Create a new item object
        inputs = {
            "item_name": item_name,
            "cost": cost,
            "subtype": subtype,
            "replacement_duration": replacement_duration,
            "dateCreated": dateCreated,
            "dateOfReplacement": dateOfReplacement,
            
        }

        # Add the new item to the inventory
        # Add your logic to add the item to the inventory here
        logger.debug(f"API call: Adding item {inputs} to inventory")
        add.addItem(inputs)

    # Render the add template
    return render_template(Constants.ADD_PAGE)


# Delete logic should be based on "primary" key.
@app.route("/inventory/delete", methods=["GET", "POST"])
def delete(productName=None):
    delete = Delete()
    logger.debug("deleting product")
    item_name = request.args.get("id")
    logger.debug(item_name)
    if item_name:
        delete.deleteData(str(item_name))    
        return redirect("/inventory/display")
 
    return render_template(Constants.DELETE_PAGE)


@app.route("/inventory/display")
def display(forecast=False,subType=None):
    # Add your logic to retrieve and display the inventory here
    display = Fetch()
    forecast = request.args.get("forecast")
    subType = request.args.get("subtype")
    logger.debug("Subtype is ", subType)
    if forecast=="true":
        info_for_html = display.fetchAllInfo(forecast=True,subType=subType)
    else:
        info_for_html = display.fetchAllInfo(forecast=False,subType=subType)
    
    #info_for_html = display.fetchAllInfo(forecast=False)
    logger.debug(info_for_html)
    
    total_cost=0
    for i in info_for_html:
        total_cost += i[Constants.ITEM.COST]
        
    return render_template(Constants.DISPLAY_PAGE, inventory=info_for_html,total_cost=total_cost)



@app.route("/inventory/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        # Handle form submission and search for items in inventory
        search_query = request.form.get("search_query")
        logger.debug("The search query is ", search_query)
        fetch = Fetch()
        
        
        info_for_html = fetch.fetchAllInfo(forecast=False,searchQuery=search_query)
        if(info_for_html!=[]):
            logger.debug(info_for_html)        
            return render_template("display.html", inventory=info_for_html)
    return render_template(Constants.SEARCH_PAGE)


@app.route("/inventory/overdue", methods=["GET", "POST"])
def overdue():
    if request.method == "GET":
        # Handle form submission and search for items in inventory
        fetch = Fetch()
        
        info_for_html = fetch.fetchAllInfo(forecast=True)
        if(info_for_html!=[]):
            logger.debug(info_for_html)        
            return jsonify(inventory=info_for_html)
    return jsonify({"error": "Invalid request"})



@app.route("/inventory/download", methods=["GET"])
def download():
    inventory = Fetch().fetchAllInfo()
    filename = Constants.CSV_FILE  # Replace with the desired file path
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Item Name", "Cost", "Subtype", "Replacement Duration",'Date Created',"Date of Replacement"])
        for item in inventory:
            writer.writerow(
                [
                    item[Constants.ITEM.NAME],
                    item[Constants.ITEM.COST],
                    item[Constants.ITEM.TYPE],
                    item[Constants.ITEM.DURATION],
                    item[Constants.ITEM.CREATION_DATE],
                    item[Constants.ITEM.REPLACEMENT_DATE]
                ]
            )
    return send_file(filename, as_attachment=True)

@app.route("/inventory/edit", methods=["GET", "POST"])
def edit(items=[]):
    display = Fetch()
    id = request.args.get("id")
    inp = display.fetchAllInfo(searchQuery=id,searchByID=True)
    logger.trace(inp[0])
    logger.trace(inp[0])
    item = {
            "id": inp[0]['id'],
            "name": inp[0]['name'],
            "cost": inp[0]['cost'],
            "subtype": inp[0]['subtype'],
            "replacementDuration": inp[0]['replacementDuration'],
            "dateCreated": inp[0]['dateCreated'],
            "dateOfReplacement": inp[0]['dateOfReplacement'],
        }
    return render_template(Constants.EDIT_PAGE, item=item)



@app.route("/inventory/update", methods=["POST"])
def update():
    
    edit = Edit()
    item_name = request.form.get("name")
    cost = request.form.get("cost")

    id = request.form["id"]
    subtype = request.form.get("subtype")
    dateCreated = request.form.get("dateCreated")
    dateCreated_date = datetime.datetime.strptime(dateCreated, "%Y-%m-%d").date()
    dateOfReplacement = dateCreated_date + (datetime.timedelta(days=int(request.form.get("replacementDuration")))*31)     
    if subtype not in Constants.ALLOWED_SUBTYPES:
        logger.error("Invalid subtype value")
        return render_template(Constants.ERROR_PAGE, message="Invalid subtype value")
    replacement_duration = request.form.get("replacementDuration")
    
    inputs = {
            "item_name": item_name,
            "cost": cost,
            "subtype": subtype,
            "replacement_duration": replacement_duration,
            "dateCreated": dateCreated,
            "dateOfReplacement": dateOfReplacement,
        } 
    edit.editItem(id, inputs)
    return redirect("/inventory")
if __name__ == "__main__":
    logger.trace("Starting the server page")
    app.run(host='0.0.0.0', port=5000, debug=False)
    logger.trace("Started the server page")
