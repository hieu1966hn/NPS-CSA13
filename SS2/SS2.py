# ### Bài thực hành 1: 
# class Point:
#     def __init__(self, x, y): # 1; 2
#        self.x = x
#        self.y = y
       
#     ## Khởi tạo phương thức cộng
#     def add(self, B_point):
#         return Point(self.x + B_point.x, self.y + B_point.y)
    
#     ## Khởi tạo phương thức cộng
#     def sub(self, B_point):
#         return Point(self.x - B_point.x, self.y - B_point.y)
    
#     ## Khởi tạo một phương thức hiển thị: __str__
#     def __str__(self):
#         return f'({self.x}; {self.y})'
    
# A = Point(1, 2)
# B = Point(3, 4)
# print(A.add(B))
# print(A.sub(B))



### Ví dụ 2: Kế thừa với Person
class Person:
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print('My name is: ', self.name)
        

class Student(Person): # child class
    def __init__(self, name, grade):
        super().__init__(name) # KẾ THỪA THUỘC TÍNH, Bao nhiêu thuộc tính muốn kế thừa thì điền vào đây
        self.grade = grade 
        
    ## Override phương thức print_name
    def print_name(self):
        print('Name: ', self.name)
        
    def print_grade(self):
        print("I am in grade: ", self.grade)
        
    
# Duong = Student("Dương", 10)
# Duong.print_name()
# Duong.print_grade()


## Chữa bài Mathlist
class MathList:
    def __init__(self, list):
        self.list = list
        
        
    def add(self, anum):
        for i in range(len(self.list)):  # 0 -> 4
            self.list[i] += anum
        return self.list
    
    def sub(self, anum):
        for i in range(len(self.list)):  # 0 -> 4
            self.list[i] -= anum
        return self.list
            
            
    def __str__(self):
        return "Final List: {}".format(self.list)

MathList1 = MathList([1, 2, 3, 4, 5])
MathList2 = MathList([1, 2, 3, 4, 5])
MathList1.add(3)
print(MathList1)
MathList2.sub(3)
print(MathList2)
    

        