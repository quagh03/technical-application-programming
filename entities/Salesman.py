from entities.Employee import Employee


class Salesman(Employee):
    def __init__(self, employee_id, name, phone_number, email, revenue, months_worked):
        position = "Nhân viên bán hàng"
        super().__init__(employee_id, name, phone_number, email, position)
        self.revenue = revenue
        self.months_worked = months_worked

