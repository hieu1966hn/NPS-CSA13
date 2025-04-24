from abc import ABC, abstractclassmethod

class MonAn(ABC):
    @abstractclassmethod
    def chuan_bi(self): # phương thức trừu tượng
        pass
    
    
class MonChinh(MonAn):
    def chuan_bi(self):
        print("Chuẩn bị món chính")
        
class MonTrangMieng(MonAn):
    def chuan_bi(self):
        print("Chuẩn bị món tráng miệng")
        
# # Tạo đối tượng và gọi phương thức
# mon_chinh = MonChinh()
# mon_chinh.chuan_bi() # kết quả: Chuẩn bị món chính


class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    def speak(self):
        pass

class Shiba(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def speak(self):
        print('gào gào')
        
class Husky(Dog):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def speak(self):
        print('Howl')
        

# Shiba1 = Shiba("Inu", 8)
# Husky1= Husky("Ngáo", 10)

# Shiba1.speak()
# Husky1.speak()


############## Bài tập tính đóng gói
import math

class Circle:
    def __init__(self, radius):
        if radius <0: 
            raise ValueError("Bán kính không thể là số âm")
        self._radius = radius
    
    # Hàm lấy bán kính được bảo vệ
    def get_radius(self):
        return self._radius
    
    # Hàm cập nhật lại giá trị bán kính
    def set_radius(self, new_radius):
        if new_radius < 0: 
            raise ValueError("Bán kính không thể là số âm")
        self._radius = new_radius
        
    def area(self):
        return math.pi * self._radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self._radius
    
## Sử dụng class
circle1 = Circle(3)
# in ra bán kính
print(circle1._radius) # VỀ LÝ thuyết là không in ra
print(circle1.get_radius())
print(circle1.perimeter())
print(circle1.area())