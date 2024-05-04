from entities.Manager import Manager
from entities.Salesman import Salesman


class ManageEmployee:
    def __init__(self):
        self.employees = []
        self.numberOfEmp = 1
        self.deletedBackup = []
        self.groups = []

    def add_employee(self):
        while True:
            num_employees = int(input("Nhập số lượng nhân viên muốn thêm: "))
            if num_employees <= 0:
                print("Số lượng nhân viên phải lớn hơn 0. Vui lòng nhập lại.")
            else:
                break
        for _ in range(num_employees):
            while True:
                print("Chọn loại nhân viên:")
                print("1. Quản lý")
                print("2. Nhân viên bán hàng")
                employee_type = input("Chọn loại nhân viên (1/2): ")

                if employee_type not in ['1', '2']:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
                    continue
                else:
                    break

            employee_id = self.numberOfEmp
            name = input("Nhập tên nhân viên: ")
            phone_number = input("Nhập số điện thoại: ")
            email = input("Nhập email: ")

            if employee_type == '1':
                management_group = input("Nhập nhóm quản lý: ")
                num_employees_in_group = int(input("Nhập số lượng nhân viên trong nhóm: "))
                total_group_revenue = float(input("Nhập tổng doanh thu của nhóm: "))
                employee = Manager(employee_id, name, phone_number, email, management_group,
                                   num_employees_in_group, total_group_revenue)
                self.employees.append(employee)
                self.numberOfEmp += 1
            elif employee_type == '2':
                revenue = float(input("Nhập doanh số bán hàng: "))
                months_worked = int(input("Nhập số tháng làm việc: "))
                employee = Salesman(employee_id, name, phone_number, email, revenue, months_worked)
                self.employees.append(employee)
                self.numberOfEmp += 1
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
                continue

            print(f"Thêm mới nhân viên {employee.employee_id} thành công!")

    def list_employees(self):
        if not self.employees:
            print("Danh sách nhân viên trống.")
            return

        print("Danh sách nhân viên:")
        print("-------------------------------------------------------------------------------------------------------")
        print("| {:<15} | {:<20} | {:<15} | {:<25} | {:<25} |".format(
            "Mã NV", "Tên", "Số điện thoại", "Email", "Chức vụ"))
        print("-------------------------------------------------------------------------------------------------------")
        for employee in self.employees:
            print("| {:<15} | {:<20} | {:<15} | {:<25} | {:<25} |".format(
                employee.employee_id, employee.name, employee.phone_number, employee.email, employee.position))
        print("-------------------------------------------------------------------------------------------------------")

    def is_empty_employee_list(self):
        if not self.employees:
            print("Danh sách nhân viên trống. Bạn phải thêm mới nhân viên trước!")
            return True
        return False

    def remove_employee(self, employee_id, backup=False):
        if self.is_empty_employee_list():
            return

        if employee_id in self.employees:
            if backup:
                self.deletedBackup.append(self.employees[employee_id])
                print(f"Xóa có back up nhân viên {employee_id} thành công!")
            del self.employees[employee_id]
            print(f"Xóa thành công nhân viên {employee_id} !")
        else:
            print("Không tìm thấy nhân viên")

    def search_employee(self, search_key):
        if self.is_empty_employee_list():
            return

        found = False

        for emp in self.employees:
            if search_key in [emp.employee_id, emp.name]:
                print(emp.__dict__)
                found = True

        if not found:
            print("Không tìm thấy nhân viên!")

    def display_by_position(self, position):
        if self.is_empty_employee_list():
            print("Danh sách nhân viên trống. Bạn phải thêm mới nhân viên trước!")
            return

        for emp in self.employees:
            if emp.position == position:
                print(emp.__dict__)

    def calculate_total_revenue(self):
        total_revenue = 0
        for emp in self.employees:
            if isinstance(emp, Salesman):
                total_revenue += emp.revenue
        return total_revenue

    def calculate_average_revenue(self):
        total_revenue = self.calculate_total_revenue()
        num_salespeople = sum(isinstance(emp, Salesman) for emp in self.employees)
        if num_salespeople == 0:
            return 0
        return total_revenue / num_salespeople

    def calculate_total_salary(self):
        total_salary = 0
        for emp in self.employees:
            if isinstance(emp, Manager):
                total_salary += 8000000 + (0.01 * emp.total_group_revenue) + emp.num_employees_in_group * 250000
            elif isinstance(emp, Salesman):
                if emp.months_worked < 6:
                    total_salary += 0.03 * emp.revenue + 2200000
                else:
                    total_salary += 0.045 * emp.revenue + 3500000
        return total_salary

    def display_top_salespeople(self, n):
        salespeople = [emp for emp in self.employees if isinstance(emp, Salesman)]
        top_salespeople = sorted(salespeople, key=lambda x: x.revenue, reverse=True)[:n]
        for emp in top_salespeople:
            print(emp.__dict__)

    def display_salary_statistics(self, option):
        if not self.employees:  # Kiểm tra nếu danh sách nhân viên rỗng
            print("Không có dữ liệu nhân viên.")
            return
        salaries = [emp.calculate_salary() for emp in self.employees]
        avg_salary = sum(salaries) / len(salaries)
        if option == "high":
            above_average_salaries = [emp for emp in self.employees if emp.calculate_salary() > avg_salary]
            for emp in above_average_salaries:
                print(emp.__dict__)
        elif option == "low":
            below_average_salaries = [emp for emp in self.employees if emp.calculate_salary() < avg_salary]
            for emp in below_average_salaries:
                print(emp.__dict__)
        elif option == "all":
            below_average_salaries = [emp for emp in self.employees if emp.calculate_salary() < avg_salary]
            above_average_salaries = [emp for emp in self.employees if emp.calculate_salary() > avg_salary]
            print("\nBelow Average Salaries:")
            for emp in below_average_salaries:
                print(emp.__dict__)
            print("\nAbove Average Salaries:")
            for emp in above_average_salaries:
                print(emp.__dict__)

    def display_highest_revenue_group(self):
        groups = {}
        for emp in self.employees:
            if isinstance(emp, Manager):
                if emp.management_group in groups:
                    groups[emp.management_group] += emp.total_group_revenue
                else:
                    groups[emp.management_group] = emp.total_group_revenue

        if not groups:
            print("Không có dữ liệu về nhóm nào.")
        else:
            if all(revenue <= 0 for revenue in groups.values()):
                max_group = "newGroup"
                max_revenue = float('-inf')
                for emp in self.employees:
                    if isinstance(emp, Manager):
                        if emp.total_group_revenue > max_revenue:
                            max_group = emp.management_group
                            max_revenue = emp.total_group_revenue
                print(f"Nhóm cao nhất đã được cập nhật doanh thu về âm: {max_group}.")
                print("Danh sách đã được cập nhật.")
                new_group = {
                    'name': max_group,
                    'total_revenue': max_revenue
                }
                self.groups.append(new_group)
                
            else:
                highest_group = max(groups, key=groups.get)
                print(f"Nhóm có tổng doanh thu cao nhất là: {highest_group}, Tổng doanh thu: {groups[highest_group]}")
