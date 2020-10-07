EMPLOYEES = [
    {
        "id": 1,
        "name": "Jack Doe",
        "department": "Human Resources",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Jane Flo",
        "department": "Software Engineering",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Alex Doe",
        "department": "Program Management",
        "locationId": 2,
        "customerId": 1
    }
]


def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
