class MonAn:
    def chuan_bi():
        print("Chuẩn bị món ăn")
        
        
class MonChinh(MonAn):
    def chuan_bi(self):
        print("Chuẩn bị món chính")
        
class MonTrangMieng(MonAn):
    def chuan_bi(self):
        print("Chuẩn bị món tráng miệng")
        

def goi_mon(mon_an: MonAn):
    mon_an.chuan_bi()
    

# mon_chinh = MonChinh()
# mon_trang_mieng = MonTrangMieng()

# goi_mon(mon_chinh)
# goi_mon(mon_trang_mieng)

### Ví dụ 2: về tính đa hình
class Dog:
    tail = "long"
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        self.__sound = 'Woof' # tính đóng gói (phải sử dụng phương thức mới lấy được giá trị này)
    
    def get_description(self):
        return f'{self.name} is {self.age}-year-old'
    
    def speak(self):
        return self.__sound
    
class Pooddle(Dog):
    tail = "short"
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def get_description(self):
        return f'{self.name} is a {self.age}-year-old pooddle'
    
class Chihuahua(Dog):
    tail = "short"
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__sound = 'đinh đinh'
        
    def get_description(self):
        return f'{self.name} is a {self.age}-year-old chihuahua'
    
    def speak(self):
        return self.__sound
    
pooddle1 = Pooddle("Schocolate", 10)
chihuahua1 = Chihuahua("Xúc xích", 5)
# print(pooddle1.get_description())
# print(pooddle1.name)
# print(pooddle1.age)
# print(pooddle1.speak())
print(chihuahua1.get_description())
print(chihuahua1.tail)
print(chihuahua1.name)
print(chihuahua1.age)
print(chihuahua1.speak())
        