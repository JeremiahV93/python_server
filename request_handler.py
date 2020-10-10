from http.server import BaseHTTPRequestHandler, HTTPServer

from animals import get_all_animals
from animals import get_single_animal
from animals import create_animal
from animals import delete_animal
from animals import update_animal


from locations import get_all_locations
from locations import get_single_location
from locations import create_location
from locations import delete_location
from locations import update_location

from employees import get_all_employees
from employees import get_single_employee
from employees import create_employee
from employees import delete_employee
from employees import update_employee

from customers import get_all_customers
from customers import get_single_customer
from customers import create_customer
from customers import delete_customer
from customers import update_customer


import json





# Here's a class. It inherits from another class.
class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {}  # Default response

        (resource, id) = self.parse_url(self.path)

        # Your new console.log() that outputs to the terminal
        print(self.path)

        # It's an if..else statement
        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_animals()}"
        elif resource == "locations":
            if id is not None:
                response = f"{get_single_location(id)}"
            else:
                response = f"{get_all_locations()}"
        elif resource == "employees":
            if id is not None:
                response = f"{get_single_employee(id)}"
            else:
                response = f"{get_all_employees()}"
        elif resource == "customers":
            if id is not None:
                response = f"{get_single_customer(id)}"
            else:
                response = f"{get_all_customers()}"
        else:
            response = []

        # This weird code sends a response back to the client
        self.wfile.write(f"{response}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Initialize new animal
        # new_animal = None
        # new_customer = "Test"

        # Add a new animal to the list. Don't worry about
        # the orange squiggle, you'll define the create_animal
        # function next.
        if resource == "animals":
            new_animal = None
            new_animal = create_animal(post_body)
            self.wfile.write(f"{new_animal}".encode())
        elif resource == "customers":
            new_customer = None
            new_customer = create_customer(post_body)
            self.wfile.write(f"{new_customer}".encode())
        elif resource == "employees":
            new_employee = None
            new_employee = create_employee(post_body)
            self.wfile.write(f"{new_employee}".encode())
        elif resource == "locations":
            new_location = None
            new_location = create_location(post_body)
            self.wfile.write(f"{new_location}".encode())



        # Encode the new animal and send in response
        # self.wfile.write(f"{new_animal}".encode())
        # self.wfile.write(f"{new_customer}".encode())

    # Delete func
    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            delete_animal(id)
        elif resource == "customers":
            delete_customer(id)
        elif resource == "employees":
            delete_employee(id)
        elif resource == "locations":
            delete_location(id)

        # Encode the new animal and send in response
        self.wfile.write("".encode())


    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        # Delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)
        elif resource == "customers":
            update_customer(id, post_body)
        elif resource == "locations":
            update_location(id, post_body)
        elif resource == "employees":
            update_employee(id, post_body)

        # Encode the new animal and send in response
        self.wfile.write("".encode())


# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()
