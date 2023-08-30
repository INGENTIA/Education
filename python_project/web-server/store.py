# Import the 'requests' library, which is used for making HTTP requests to web servers.
import requests

# Define a function named 'get_categories' that retrieves and prints information about categories.
def get_categories():
    # Send an HTTP GET request to the specified URL to fetch data about categories.
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    
    # Print the HTTP status code of the response.
    print(r.status_code)
    
    # Print the content of the response, which likely contains information about categories.
    print(r.text)

    categories = r.json()
    for category in categories:
        print(category['name'])


# End of the function definition.