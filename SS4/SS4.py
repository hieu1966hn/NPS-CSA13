# ## KHỞI TẠO SET
# fruit_basket = {'apple', 'banana', 'cherry', 'apple'}
# print(f"Tập hợp Set vừa khởi tạo là: {fruit_basket}")


# # Thêm phần tử: 
# # fruit_basket.add("orange") # add: thêm từng phần tử

# # Or
# fruit_basket.update({'orange', 'kiwi'})
# print('rổ hoa quả sau khi thêm phần tử là: ' ,fruit_basket)

# ## Xóa phần tử
# fruit_basket.remove('apple')

# # or
# fruit_basket.discard("apple")





#### phép hợp 

lunch = {'soup', 'sandwich', 'omelet'}
dinner = {'soup', 'steak'}
# meals = lunch.union(dinner) # phép hợp
# print(f'Hợp bữa trưa và tối là {meals}')


### PHÉP GIAO
# meals_giao = lunch & dinner
# print(meals_giao)

### PHÉP TRỪ
# meals_tru = lunch.intersection(dinner)
# print(meals_tru)



##### Bài tập ánh xạ
# sample_input = [5.0, 7.0, 8.0, 10.0, 9.0] # hệ 10

# sample_output = []

# for i in sample_input:
#     x = (i*4)/10
#     # thêm một phần tử vào mảng output
#     sample_output.append(x)

# print(f'Hệ được chuyển đổi từ 10 => 4 là: {sample_output}')


### Giải bài tập chuyển đổi hệ 10 => hệ 4 với ánh xạ (maping)
# x = [5.0, 7.0, 8.0, 10.0, 9.0] # hệ 10

# y = map(lambda gpa: gpa*4/10, x)
# print(f'hệ 4 {list(y)} được ánh xạ từ hệ 10 {x} ')



### Thực hành 2 với map
# students = ["Hiếu", "Dương", "Vy"]
# ## Viết hoa toàn bộ nội dung bên trong danh sách
# students_upper = list(map(lambda uppper_case: uppper_case.upper() , students)) ## Ép kiểu về danh sách.
# print(f'Danh sách mới được viết hoa hết các phần tử là: {list(students_upper)}')


### Thực hành với map - dict
NPS_CSA13 = {
    'hv1': 'Hồng Dương',
    'hv2': "Trung Hiếu"
}
# print(NPS_CSA13.get("hv1"))
#Yêu cầu: Viết hoa tất cả giá trị
uppercase_students = dict(
    map(lambda item: (item[0], item[1].upper()) , NPS_CSA13.items())
)
print(uppercase_students) ## Nghiên cứu thêm


