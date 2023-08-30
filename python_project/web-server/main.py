# Import the 'store' module, which contains functions and code related to managing a store's data.
import store

# Import the 'FastAPI' class from the 'fastapi' module.
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# Create an instance of the 'FastAPI' class.
app = FastAPI()

# Define a route for the root URL ("/") using the HTTP GET method.
@app.get('/')
def get_list():
    # Return a list containing the values 1, 2, and 3 as the response data.
    return [1, 2, 3]

# Define a route for the "/contact" URL using the HTTP GET method.
@app.get('/contact', response_class = HTMLResponse)
def get_list():
    # Return a dictionary with a single key 'name' and value 'INGENTIA' as the response data.
    return """
        <h1> Hello I'm a Page </h1>
        <p> soy un parrafo </p>
    
    """



# Define a function named 'run' that calls the 'get_categories' function from the 'store' module.
def run():
    # Call the 'get_categories' function to retrieve and potentially process categories data.
    store.get_categories()

# Check if this script is being run as the main program.
if __name__ == '__main__':
    # If the script is executed directly (not imported as a module), execute the 'run' function.
    run()