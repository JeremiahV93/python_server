LOCATIONS = [
    {
        "id": 1,
        "name": "Central Wing",
        "City": "Nashville",
        "address": "301 Plus Park Blvd",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "West Wing",
        "City": "Clarksville",
        "address": "1248 Wilma Rodoulph Blvd",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "East Wing",
        "City": "Knoxville",
        "address": "301 Plus Park Blvd",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_locations():
    return LOCATIONS


def get_single_location(id):
    requested_locaton = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location

def create_location(location):
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location

def delete_location(id):
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            LOCATIONS.pop(index)
            break
def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location['id'] == id:
            LOCATIONS[index] = new_location
            break
