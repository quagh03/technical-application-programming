class Employee:
    def __init__(self, employee_id, name, phone_number, email, position):
        self.employee_id = employee_id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.position = position

    def calculate_salary(self):
        raise NotImplementedError("Implement hàm này để tính lương")