import re

from entities.Manager import Manager
from entities.Salesman import Salesman


def validate_phone_number(phone_number):
    pattern = r'^[0-9]{10}$'
    return re.match(pattern, phone_number) is not None


def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_integer(input_str):
    try:
        num = int(input_str)
        if num < 0:
            print("Số phải lớn hơn 0. Vui lòng nhập lại.")
            return False
        return True
    except ValueError:
        return False


def is_float(input_str):
    try:
        num = float(input_str)
        if num <= 0:
            print("Số phải lớn hơn 0. Vui lòng nhập lại.")
            return False
        return True
    except ValueError:
        return False


class ManageEmployee:
    def __init__(self):
        self.employees = []
        self.numberOfEmp = 1
        self.deletedBackup = []
        self.groups = []

    def add_employee(self):
        while True:
            input_str = input("Nhập số lượng nhân viên muốn thêm: ")
            if is_integer(input_str):
                num_employees = int(input_str)
                break
            else:
                print("Vui lòng nhập lại một số nguyên dương.")

        for _ in range(num_employees):
            while True:
                print("Chọn chức vụ nhân viên:")
                print("1. Quản lý")
                print("2. Nhân viên bán hàng")
                employee_type = input("Chọn loại nhân viên (1/2): ")

                if employee_type not in ['1', '2']:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
                    continue
                else:
                    break

            employee_id = self.numberOfEmp
            name = input("Nhập tên: ")
            while True:
                phone_number = input("Nhập số điện thoại: ")
                if not validate_phone_number(phone_number):
                    print("Số điện thoại không hợp lệ. Vui lòng nhập lại.")
                    continue
                break

            while True:
                email = input("Nhập email: ")
                if not validate_email(email):
                    print("Email không hợp lệ. Vui lòng nhập lại.")
                    continue
                break

            if employee_type == '1':
                while True:
                    management_group = input("Nhập nhóm quản lý: ")
                    if is_integer(management_group):
                        management_group = int(management_group)
                        break
                    else:
                        print("Vui lòng nhập lại một số nguyên dương!")
                while True:
                    num_employees_in_group = input("Nhập số lượng nhân viên trong nhóm: ")
                    if is_integer(num_employees_in_group):
                        num_employees_in_group = int(num_employees_in_group)
                        break
                    else:
                        print("Vui lòng nhập lại một số nguyên dương!")
                while True:
                    total_group_revenue = input("Nhập tổng doanh thu của nhóm: ")
                    if is_float(total_group_revenue):
                        total_group_revenue = float(total_group_revenue)
                        break
                    else:
                        print("Vui lòng nhập lại một số hoợp lệ!")
                employee = Manager(employee_id, name, phone_number, email, management_group,
                                   num_employees_in_group, total_group_revenue)
                self.employees.append(employee)
                self.numberOfEmp += 1
            elif employee_type == '2':
                while True:
                    revenue = input("Nhập doanh số bán hàng: ")
                    if is_float(revenue):
                        revenue = float(revenue)
                        break
                    else:
                        print("Vui lòng nhập lại một số hoợp lệ!")
                while True:
                    months_worked = input("Nhập số tháng làm việc: ")
                    if is_integer(months_worked):
                        months_worked = int(months_worked)
                        break
                    else:
                        print("Vui lòng nhập lại một số nguyên dương!")
                employee = Salesman(employee_id, name, phone_number, email, revenue, months_worked)
                self.employees.append(employee)
                self.numberOfEmp += 1
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
                continue
            print(f"Thêm mới nhân viên {employee.employee_id} thành công!")

    def edit_employee(self, employee_id):
        if self.is_empty_employee_list():
            return
        for emp in self.employees:
            if emp.employee_id == employee_id:
                print("Chọn thông tin bạn muốn sửa:")
                print("1. Tên")
                print("2. Số điện thoại")
                print("3. Email")
                print("4. Chức vụ")
                if isinstance(emp, Manager):
                    print("5. Nhóm quản lý")
                    print("6. Số lượng nhân viên trong nhóm")
                    print("7. Tổng doanh thu của nhóm")
                elif isinstance(emp, Salesman):
                    print("5. Doanh số bán hàng")
                    print("6. Số tháng làm việc")
                if emp.employee_id == employee_id:
                    if isinstance(emp, Manager):
                        choice = input("Chọn thông tin bạn muốn sửa (0-7): ")
                    else:
                        choice = input("Chọn thông tin bạn muốn sửa (0-6): ")
                if choice == "1":
                    new_name = input("Nhập tên mới: ")
                    emp.name = new_name
                    print("Tên đã được cập nhật thành công!")
                elif choice == "2":
                    while True:
                        new_email = input("Nhập email mới: ")
                        if not validate_email(new_email):
                            print("Email không hợp lệ. Vui lòng nhập lại.")
                            continue
                        emp.email = new_email
                        print("Email đã được cập nhật thành công!")
                        break
                elif choice == "3":
                    while True:
                        new_phone_number = input("Nhập số điện thoại mới: ")
                        if not validate_phone_number(new_phone_number):
                            print("Số điện thoại không hợp lệ. Vui lòng nhập lại.")
                            continue
                        emp.phone_number = new_phone_number
                        print("Số điện thoại đã được cập nhật thành công!")
                        break
                elif choice == "4":
                    print("Chức vụ mới: ")
                    print("1. Quản lý")
                    print("2. Nhân viên bán hàng")
                    new_position = input("Chọn (1/2): ")
                    if new_position not in ['1', '2']:
                        print("Lựa chọn không hợp lệ. Vui lòng chọn lại!")
                        continue
                    else:
                        emp.position = "Quản lý" if new_position == '1' else "Nhân viên bán hàng"
                        print("Chức vụ đã được cập nhật thành công!")
                        break
                elif choice == "5" and isinstance(emp, Manager):
                    while True:
                        new_management_group = input("Nhập mới nhóm quản lý: ")
                        if is_integer(new_management_group):
                            new_management_group = int(new_management_group)
                            break
                        else:
                            print("Vui lòng nhập lại một số nguyên dương.")
                    emp.management_group = new_management_group
                    print("Nhóm quản lý đã được cập nhật thành công!")
                elif choice == "6" and isinstance(emp, Manager):
                    while True:
                        new_num_employees_in_group = input("Nhập mới số lượng nhân viên: ")
                        if is_integer(new_num_employees_in_group):
                            new_num_employees_in_group = int(new_num_employees_in_group)
                            break
                        else:
                            print("Vui lòng nhập lại một số nguyên dương.")
                    emp.num_employees_in_group = new_num_employees_in_group
                    print("Số lượng nhân viên trong nhóm đã được cập nhật thành công!")
                elif choice == "7" and isinstance(emp, Manager):
                    while True:
                        new_total_group_revenue = input("Nhập mới tổng doanh thu của nhóm: ")
                        if is_float(new_total_group_revenue):
                            new_total_group_revenue = float(new_total_group_revenue)
                            break
                        else:
                            print("Vui lòng nhập lại một số hoợp lệ!")
                    emp.total_group_revenue = new_total_group_revenue
                    print("Tổng doanh thu của nhóm đã được cập nhật thành công!")
                elif choice == "5" and isinstance(emp, Salesman):
                    while True:
                        new_revenue = input("Nhập mới doanh số bán hàng: ")
                        if is_float(new_revenue):
                            new_revenue = float(new_revenue)
                            break
                        else:
                            print("Vui lòng nhập lại một số hoợp lệ!")
                    emp.revenue = new_revenue
                    print("Doanh số bán hàng đã được cập nhật thành công!")
                elif choice == "6" and isinstance(emp, Salesman):
                    while True:
                        new_months_worked = input("Nhập mới số tháng làm việc: ")
                        if is_integer(new_months_worked):
                            new_months_worked = int(new_months_worked)
                            break
                        else:
                            print("Vui lòng nhập lại một số nguyên dương.")
                    emp.months_worked = new_months_worked
                    print("Số tháng làm việc đã được cập nhật thành công!")
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng thử lại!")
                return
        print(f"Không tìm thấy nhân viên có mã số {employee_id}!")

    def list_employees(self):
        if not self.employees:
            print("Danh sách nhân viên trống. Hãy thêm mới!")
            return True

        print("Danh sách nhân viên:")
        print("--------------------------------------------------------------------------------------------------------------------")
        print("| {:<15} | {:<20} | {:<15} | {:<25} | {:<25} |".format(
            "Mã NV", "Tên", "Số điện thoại", "Email", "Chức vụ"))
        print("--------------------------------------------------------------------------------------------------------------------")
        for employee in self.employees:
            if employee not in self.deletedBackup:
                print("| {:<15} | {:<20} | {:<15} | {:<25} | {:<25} |".format(
                    employee.employee_id, employee.name, employee.phone_number, employee.email, employee.position))
        print("--------------------------------------------------------------------------------------------------------------------")

    def is_empty_employee_list(self):
        if not self.employees:
            print("Danh sách nhân viên trống. Bạn phải thêm mới nhân viên trước!")
            return True
        return False

    def remove_employee(self, employee_id):
        if self.is_empty_employee_list():
            return

        found_employee = None
        for emp in self.employees:
            if emp.employee_id == employee_id:
                found_employee = emp
                break

        if found_employee:
            print(
                f"Bạn đang thực hiện trên nhân viên: Mã nhân viên: {found_employee.employee_id}, Tên nhân viên: {found_employee.name}, Chức vụ: {found_employee.position}")
            choice = input("Bạn có muốn sao lưu thông tin nhân viên trước khi xóa? (y/n): (hoặc 'q' để thoát) ")
            if choice.lower() == 'q':
                print("Thoát khỏi chức năng xóa nhân viên.")
                return
            elif choice.lower() == 'y':
                self.deletedBackup.append(found_employee)
                print(f"Thao tác xóa và sao lưu thực hiện thành công!")
            else:
                confirm_delete = input("Bạn có chắc chắn muốn xóa nhân viên này? (y/n): (hoặc 'q' để thoát) ")
                if confirm_delete.lower() == 'q':
                    print("Thoát khỏi chức năng xóa nhân viên.")
                    return
                elif confirm_delete.lower() == 'y':
                    self.employees.remove(found_employee)
                    print(f"Thao tác xóa thực hiện thành công!")
                else:
                    print("Hủy bỏ xóa nhân viên.")
        else:
            print(f"Không tìm thấy nhân viên có mã số {employee_id}!")

    def search_employee(self):
        if self.is_empty_employee_list():
            return

        while True:
            print("Chọn chức năng tìm kiếm:")
            print("1. Tìm kiếm theo mã nhân viên")
            print("2. Tìm kiếm theo tên nhân viên")
            option = input("Chọn chức năng (1/2): ")

            if option == "1":
                search_key = input("Nhập mã nhân viên cần tìm kiếm: ")
                found = False
                for emp in self.employees:
                    if str(emp.employee_id) == search_key:
                        print("Thông tin nhân viên được tìm thấy:")
                        print(f"Mã NV: {emp.employee_id}")
                        print(f"Tên: {emp.name}")
                        print(f"Số điện thoại: {emp.phone_number}")
                        print(f"Email: {emp.email}")
                        print(f"Chức vụ: {emp.position}")
                        if isinstance(emp, Manager):
                            print(f"Nhóm quản lý: {emp.management_group}")
                            print(f"Số lượng nhân viên trong nhóm: {emp.num_employees_in_group}")
                            print(f"Tổng doanh thu của nhóm: {emp.total_group_revenue}")
                        elif isinstance(emp, Salesman):
                            print(f"Doanh số bán hàng: {emp.revenue}")
                            print(f"Số tháng làm việc: {emp.months_worked}")
                        found = True
                        break
                if not found:
                    print("Không tìm thấy nhân viên có mã số", search_key)
                break
            elif option == "2":
                search_key = input("Nhập tên nhân viên cần tìm kiếm: ").lower()
                found = False
                for emp in self.employees:
                    if search_key in emp.name.lower():
                        print("Thông tin nhân viên được tìm thấy:")
                        print(f"Mã NV: {emp.employee_id}")
                        print(f"Tên: {emp.name}")
                        print(f"Số điện thoại: {emp.phone_number}")
                        print(f"Email: {emp.email}")
                        print(f"Chức vụ: {emp.position}")
                        if isinstance(emp, Manager):
                            print(f"Nhóm quản lý: {emp.management_group}")
                            print(f"Số lượng nhân viên trong nhóm: {emp.num_employees_in_group}")
                            print(f"Tổng doanh thu của nhóm: {emp.total_group_revenue}")
                        elif isinstance(emp, Salesman):
                            print(f"Doanh số bán hàng: {emp.revenue}")
                            print(f"Số tháng làm việc: {emp.months_worked}")
                        found = True
                if not found:
                    print("Không tìm thấy nhân viên có tên", search_key)
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

    def display_by_position(self, position):

        employees_at_position = [emp for emp in self.employees if emp.position == position]
        if not employees_at_position:
            print("Không có nhân viên ở vị trí đã cho.")
            return

        print("Danh sách nhân viên ở vị trí", position)
        print(
            "--------------------------------------------------------------------------------------------------------------------")
        print("| {:<15} | {:<20} | {:<15} | {:<25} | {:<25} |".format(
            "Mã NV", "Tên", "Số điện thoại", "Email", "Chức vụ"))
        print(
            "--------------------------------------------------------------------------------------------------------------------")
        for emp in employees_at_position:
            print("| {:<15} | {:<20} | {:<15} | {:<25} | {:<25} |".format(
                emp.employee_id, emp.name, emp.phone_number, emp.email, emp.position))
        print(
            "--------------------------------------------------------------------------------------------------------------------")

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
            # if isinstance(emp, Manager):
            #     total_salary += 8000000 + (0.01 * emp.total_group_revenue) + emp.num_employees_in_group * 250000
            # elif isinstance(emp, Salesman):
            #     if emp.months_worked < 6:
            #         total_salary += 0.03 * emp.revenue + 2200000
            #     else:
            #         total_salary += 0.045 * emp.revenue + 3500000
            total_salary += emp.calculate_salary()
        return total_salary

    def display_top_salespeople(self, n):
        salespeople = [emp for emp in self.employees if isinstance(emp, Salesman)]
        top_salespeople = sorted(salespeople, key=lambda x: x.revenue, reverse=True)[:n]
        for emp in top_salespeople:
            print(emp.__dict__)

    def display_salary_statistics(self, option):
        if not self.employees:
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
