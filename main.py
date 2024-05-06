import os

from entities.ManageEmployee import ManageEmployee


def display_menu():
    print("******************************************************************************************")
    print("*                        Nhom 3 | 66PM3 | Quản Lý Nhân Sự Cửa Hàng                       *")
    print("* 1. Thêm mới nhân viên                                                                  *")
    print("* 2. Sửa thông tin nhân viên                                                             *")
    print("* 3. Xóa nhân viên                                                                       *")
    print("* 4. Tìm kiếm nhân viên                                                                  *")
    print("* 5. Hiển thị danh sách nhân viên theo vị trí công việc                                  *")
    print("* 6. Tính tổng doanh thu và doanh thu trung bình của cửa hàng trong tháng hiện tại       *")
    print("* 7. Tính tổng lương cửa hàng phải trả cho nhân viên trong tháng hiện tại                *")
    print("* 8. Sắp xếp danh sách n nhân viên có doanh thu cao nhất                                 *")
    print("* 9. Thống kê danh sách nhân viên có mức lương thấp hoặc cao hơn mức lương trung bình    *")
    print("* 10. Hiển thị nhóm có tổng doanh thu cao nhất                                           *")
    print("* 11. Hiển thị danh sách tất cả nhân viên                                                *")
    print("* 12. Thoát chương trình                                                                 *")
    print("******************************************************************************************")


def main():
    manage_employee = ManageEmployee()

    while True:
        display_menu()
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            # Thêm nhân viên
            manage_employee.add_employee()
            input("Nhấn Enter để trở về menu!")
        elif choice == "2":
            # Sửa thông tin nhân viên
            if manage_employee.is_empty_employee_list():
                continue
            else:
                manage_employee.list_employees()
                employee_id_str = input("Nhập mã số nhân viên muốn sửa thông tin: ")
                manage_employee.edit_employee(employee_id_str)
                manage_employee.list_employees()
            input("Nhấn Enter để trở về menu!")
        elif choice == "3":
            # Xóa nhân viên
            if manage_employee.is_empty_employee_list():
                continue
            else:
                manage_employee.list_employees()
                employee_id = int(input("Nhập mã số nhân viên muốn xóa: "))
                manage_employee.remove_employee(employee_id)
            input("Nhấn Enter để trở về menu!")
        elif choice == "4":
            # Tìm kiếm nhân viên
            manage_employee.search_employee()
            input("Nhấn Enter để trở về menu!")
        elif choice == "5":
            manage_employee.list_employees()
            input("Nhấn Enter để trở về menu!")
        elif choice == "6":
            # Tính tổng doanh thu và doanh thu trung bình của cửa hàng trong tháng hiện tại
            total_revenue = manage_employee.calculate_total_revenue()
            avg_revenue = manage_employee.calculate_average_revenue()
            print(f"Tổng doanh thu của cửa hàng trong tháng hiện tại là: {total_revenue}")
            print(f"Doanh thu trung bình của cửa hàng trong tháng hiện tại là: {avg_revenue}")
            pass
        elif choice == "7":
            # Tính tổng lương cửa hàng phải trả cho nhân viên trong tháng hiện tại
            total_salary = manage_employee.calculate_total_salary()
            if total_salary == 0:
                print("Không có dữ liệu về lương nhân viên trong tháng hiện tại.")
            else:
                print(f"Tổng lương cửa hàng phải trả cho nhân viên trong tháng hiện tại là: {total_salary}")
            pass
        elif choice == "8":
            # Sắp xếp danh sách n nhân viên có doanh thu cao nhất
            while True:
                try:
                    n = int(input("Nhập số lượng nhân viên có doanh thu cao nhất bạn muốn hiển thị: "))
                    if n <= 0:
                        print("Số lượng nhân viên cần hiển thị phải lớn hơn 0. Vui lòng nhập lại.")
                    else:
                        break
                except ValueError:
                    print("Vui lòng nhập một số nguyên.")

            if n > len(manage_employee.employees):
                print("Số lượng nhân viên yêu cầu hiển thị vượt quá tổng số nhân viên. Hiển thị tất cả nhân viên có doanh thu cao nhất.")
                n = len(manage_employee.employees)
            
            top_salespeople = sorted(manage_employee.employees, key=lambda x: x.revenue, reverse=True)[:n]
            for emp in top_salespeople:
                print(emp.__dict__)
            pass
        elif choice == "9":
            # Thống kê danh sách nhân viên có mức lương thấp hoặc cao hơn mức lương trung bình
            print("Vui lòng chọn tùy chọn để thống kê:")
            print("1. Lương thấp hơn mức lương trung bình (low)")
            print("2. Lương cao hơn mức lương trung bình (high)")
            print("3. Tất cả (all)")
            
            option = input("Nhập từ khóa low, high, all: ")
            if option.lower() not in ['low', 'high', 'all']:
                print("Lựa chọn không hợp lệ. Vui lòng chọn 'low', 'high' hoặc 'all'.")
            else:
                manage_employee.display_salary_statistics(option.lower())
            pass
        elif choice == "10":
            # Hiển thị nhóm có tổng doanh thu cao nhất
            manage_employee.display_highest_revenue_group()
            pass
        elif choice == "11":
            manage_employee.list_employees()
            pass
        elif choice == "12":
            print("Chương trình kết thúc.")
            break
        else:
            os.system('cls')
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
