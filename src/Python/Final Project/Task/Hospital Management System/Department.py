"""
this is the Department class in hospital management system
this class is responsible for managing the departments in the hospital

it has the following attributes:
- name: the name of the department

it has the following methods:
- add_patient: adds a patient to the department
- add_staff: adds a staff member to the department
"""

class Department:
    # this is the constructor method for the Department class
    def __init__(self, name):
        self.name = name
        self.staff = []
        self.patients = []

    # this method adds a patient to the department, it takes a patient object as a parameter and appends it to the patients list
    def add_patient(self, patient):
        self.patients.append(patient)

    # this method adds a staff member to the department, it takes a staff member object as a parameter and appends it to the staff list
    def add_staff(self, staff_member):
        self.staff.append(staff_member)
