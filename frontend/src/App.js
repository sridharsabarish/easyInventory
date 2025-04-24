import logo from './logo.svg';
import './App.css';


function List(props){
  const stuff = props.stuff;
  return (
  <li>{stuff}</li>
);
}
function App() {
  return (
    // <section>
    // <List stuff="Hello World" />
    // <List stuff="Funny story" />
    // <List stuff="Crazy world" />
    // <List stuff="Hi there" />
    // </section>


    <div class="container">
        <h1>Add Item</h1>
        <form action="/inventory/add" method="POST">
            <div class="form-group">
                <label for="name">Item Name:</label>
                <input type="text" id="name" name="name" required/>
            </div>
            <div class="form-group">
                <label for="cost">Cost:</label>
                <input type="number" id="cost" name="cost" required/>
            </div>
            <div class="form-group">
                <label for="subtype">Subtype:</label>
                <select id="subtype" name="subtype" required>
                    <option value="Electronics">Electronics</option>
                    <option value="Household">Household</option>
                    <option value="Books">Books</option>
                    <option value="Clothes">Clothes</option>
                </select>
            </div>
            <div class="form-group">
                <label for="replacementDuration">Replacement Duration:</label>
                <input type="text" id="replacementDuration" name="replacementDuration" required/>
            </div>
            <div class="form-group">
                <label for="dateCreated">Date Created:</label>
                <input type="date" id="dateCreated" name="dateCreated" required/>
            </div>
            <button type="submit" class="btn btn-primary">Add Item</button>
            <button type="button" onclick="window.location.href='/inventory'" class="btn btn-secondary">Back</button>
        </form>
    </div>







  );
}

export default App;
