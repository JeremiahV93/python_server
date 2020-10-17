from models.location import Location
import sqlite3
import json

LOCATIONS = [
    Location(1, "Central Wing", "301 Plus Park"),
    Location(2, "West Wing", "1248 Wilma Rodoulph Blvd"),
    Location(3, "East Wing", "301 Plus Park")
]


def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        locations = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            location = Location(row['id'], row['name'], row['address'])
            locations.append(location.__dict__)

    return json.dumps(locations)


def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)

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
