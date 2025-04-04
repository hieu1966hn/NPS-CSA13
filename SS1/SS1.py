# ## khởi tạo class bộ đếm
# class Counter:
#     def __init__(self): # hàm khởi tạo
#         self.count = 0 # khởi tạo giá trị thuộc tính count mặc định = 0
        
#     def tick(self):
#         self.count += 1
        
#     def reset(self):
#         self.count = 0
        
        
# counter1 = Counter()  # Khởi tạo bộ đếm 1
# counter1.tick()
# counter1.tick()
# counter1.tick()

# print(counter1.count) ## 3

# counter1.reset() # Gọi hàm reset

# print(counter1.count) ## 0

        
        
### Định nghĩa lớp hình chữ nhật: gồm các thuộc tính, phương thức đi kèm
# class Rectangle:
#     # hàm khởi tạo thuộc tính
#     def __init__(self, width, height): ## 8, 4
#         self.width = width
#         self.height = height
    
#     # Xây dựng phương thức
#     def calculate_perimeter(self):
#         return (self.width + self.height) * 2
    
#     def calculate_area(self):
#         return self.width * self.height
    
# ### Khởi tạo đối tượng hình chữ nhật
# HCN1 = Rectangle(8, 4)
# HCN2 = Rectangle(4, 4)

# # in ra diện tích và chu vi HCN1
# print(HCN1.calculate_perimeter()) # 24
# print(HCN1.calculate_area()) # 32

# # In ra chiều dài và rộng của HCN1 ?
# print(HCN1.width)
# print(HCN1.height)

class Circle:
    def __init__(self, r):
        self.r = r
        self.PI = 3.14
    
    def calculate_perimeter(self):
        return 2 * self.PI * self.r
    
    
    def calculate_area(self):
        return self.PI * self.r * self.r

shape_name = input("Please input shape name")
if shape_name == 'circle':
    r = float(input("Please input your Radius: "))
    circle1 = Circle(r) # khởi tạo 1 đối tượng tên "cirlce1" với kiểu dữ liệu là "Hình tròn". R - bán kính được truyền vào cho hình tròn
    print("Perimeter {}".format(circle1.calculate_perimeter()))
    print("Area {}".format(circle1.calculate_area()))
