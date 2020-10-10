EMPLOYEES = [
    {
        "id": 1,
        "name": "Jack Doe",
        "department": "Human Resources",
        "manager": False,
        "full_time": True,
        "hourly_rate": 20,
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Jane Flo",
        "department": "Software Engineering",
        "manager": True,
        "full_time": True,
        "hourly_rate": 35,
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Alex Doe",
        "department": "Program Management",
        "manager": False,
        "full_time": False,
        "hourly_rate": 17,
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

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee['id'] = new_id
    EMPLOYEES.append(employee)
    return employee

def delete_employee(id):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES.pop(index)
            break


def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
