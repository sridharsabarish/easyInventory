# Inventory Manager

## Supported Functions
1. Insert Items
2. Delete Items.
2. Export CSV
3. Search
4. Display

## Project Goal

  **A webapp that allows inventory to be tracked**

### Future
- AI Integration
  - Computer Vision to identify a particular Object and suggest that to user
- Microservices
  - Testing the product inside a Docker Container?
## Usage

### Flask based deployment
Start the flask app using 

`python app.py`
The app will be running in a port `5000`, in localhost for example `http://127.0.0.1:5000`
`python3 InventoryManger.py`
|Useful APIs|Function|
|---|---|
| http://127.0.0.1:5000/inventory| Webapp's Menu Page|
| http://127.0.0.1:5000/inventory/add| Add item to inventory|
|http://127.0.0.1:5000/inventory/display| Display all items in inventory |




### Menu Based Deployment

To test with menu based deployement try the following commands.

<pre>python inventorManager.py</pre>
---

**Prompts**

1. INSERT
2. DISPLAY
3. EXPORT_CSV
4. DELETE
5. READ_CSV
6. EXIT
8. SEARCH

## Running Tests

To run the tests, use the following command:

<pre>python3 testInventoryManger.py</pre> 