from entities.Employee import Employee


class Manager(Employee):
    def __init__(self, employee_id, name, phone_number, email, management_group, num_employees_in_group,
                 total_group_revenue):
        position = "Quản Lý"
        super().__init__(employee_id, name, phone_number, email, position)
        self.management_group = management_group
        self.num_employees_in_group = num_employees_in_group
        self.total_group_revenue = total_group_revenue
