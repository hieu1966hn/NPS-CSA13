## chữa bài CP1 bài thực hành 1:
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []
         
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def calculate_average(self):
        if not self.grades:
            return 0
        # return sum(self.grades)/len(self.grades)
        s = 0
        for i in self.grades:
            s += i
        return s/len(self.grades)
    
class GradeManager:
    def __init__(self):
        self.students = []
    
    def add_student(self, name):
        # kiểm tra nếu học viên đó đã tồn tại
        if any(student.name == name for student in self.students):
            print(f'Học viên {name} đã tồn tại.')
        else:
            self.students.append(Student(name))
            print(f'Đã thêm thành công học viên {name}.')
    
    def record_grade(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                print(f'Đã thêm điểm {grade} cho {name}')
                return # thoát khỏi chương trình
        print(f'Không tìm thấy học viên {name}.')
    
    def calculate_average_all(self):
        if not self.students:
            return 0
        total = 0
        for student in self.students:
            total += student.calculate_average()
        return total/len(self.students)
            
        
### Giao diện người dùng main()
def main(): 
    manager = GradeManager()
    
    while True:
        print('\n MENU QUẢN LÝ ĐIỂM')
        print('1. Thêm học viên mới')
        print('2. Ghi điểm cho học viên')
        print('3. Tính điểm trung bình toàn bộ học viên')
        print('4. Lưu dữ liệu vào file')
        print('5. Thoát')
        
        choice = input("nhập lựa chọn của bạn (1-5):")
        if choice == '1':
            name = input('Nhập tên học viên: ')
            manager.add_student(name)
        elif choice == '2':
            name = input('Nhập tên học viên muốn thêm điểm: ')
            grade = float(input("Nhập điểm: "))
            manager.record_grade(name, grade)
        elif choice == "3":
            avg = manager.calculate_average_all()
            print(f'Điểm trung bình toàn bộ học viên: {avg:.2f}')
        # elif choice == "4":
        elif choice == "5":
            print("Thoát chương trình.")
            break
        else: 
            print("Lựa chọn không hợp lệ. Hãy chọn từ 1 - 5 ")

main()
            
            