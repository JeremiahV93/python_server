LOCATIONS = [
    {
        "id": 1,
        "name": "Central Wing",
        "City": "Nashville",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "West Wing",
        "City": "Clarksville",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "East Wing",
        "City": "Knoxville",
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
