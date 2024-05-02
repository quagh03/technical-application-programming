import os

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
    print("* 11. Thoát chương trình                                                                 *")
    print("******************************************************************************************")


def main():
    while True:
        display_menu()
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            pass
        elif choice == "2":
            # Sửa thông tin nhân viên
            pass
        elif choice == "3":
            # Xóa nhân viên
            pass
        elif choice == "4":
            # Tìm kiếm nhân viên
            pass
        elif choice == "5":
            # Hiển thị danh sách nhân viên theo vị trí công việc
            pass
        elif choice == "6":
            # Tính tổng doanh thu và doanh thu trung bình của cửa hàng trong tháng hiện tại
            pass
        elif choice == "7":
            # Tính tổng lương cửa hàng phải trả cho nhân viên trong tháng hiện tại
            pass
        elif choice == "8":
            # Sắp xếp danh sách n nhân viên có doanh thu cao nhất
            pass
        elif choice == "9":
            # Thống kê danh sách nhân viên có mức lương thấp hoặc cao hơn mức lương trung bình
            pass
        elif choice == "10":
            # Hiển thị nhóm có tổng doanh thu cao nhất
            pass
        elif choice == "11":
            print("Chương trình kết thúc.")
            break
        else:
            os.system('cls')
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
