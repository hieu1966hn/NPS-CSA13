stack = [1, 2, 3]
print(stack[-1]) # Xem phần tử cuối cùng của stack


## Thêm phần tử vào stack
stack.append(4) # 1, 2, 3, 4

## Xóa phần tử từ đỉnh stack (đuôi): pop
stack.pop() # 1, 2, 3 

## Kiểm tra danh sách rỗng với hàm len
def is_empty(stack):
    if len(stack) == 0: # if True: 
        return True
    return False

# stack_zero = []
# if len(stack_zero) == 0:
#     print(f"stack/list stack_zero đang là danh sách rỗng")
# print(is_empty(stack_zero)) ## True



#### Thực hành với OOP: Ứng dụng trình duyệt
class Browser: 
    # hàm khởi tạo
    def __init__(self):
        self.back_stack = [] # gg, ... ins, face
        self.forward_stack = []
    
    
    ### Viết phương thức: 
    # visit_page
    def visit_page(self, url):
        self.back_stack.append(url)
        #clear toàn bộ forward
        self.forward_stack.clear()
        print(f'Visiting: {url}')
    
    def back(self):
        if len(self.back_stack) > 1:
            current_page = self.back_stack.pop() # ins,facebook
            self.forward_stack.append(current_page) # [facbook]
            # để biết được mình sẽ back về trang nào?
            previous_page = self.back_stack[-1] # ins
            print(f'Going back to: {previous_page}')
        else:
            print("Canot go back")
    
    def forward(self):
        if self.forward_stack: # nếu tồn tại phần tử
            next_page = self.forward_stack.pop()
            self.back_stack.append(next_page)
            print(f'Going forward to: {next_page}')
        else:
            print("Cannot go forward.")

## Example
browser = Browser()

# truy cập vào các trang sau
print(browser.visit_page('https://www.google.com.vn/')) # Visiting: https://www.google.com.vn/
print(browser.visit_page('https://www.youtube.com/'))   # Visiting: https://www.youtube.com/
print(browser.visit_page('https://stackoverflow.com/questions')) # Visiting: https://stackoverflow.com/questions

print(browser.back())   # Going back to: https://www.youtube.com/
print(browser.back())   # Going back to: https://www.google.com.vn/
print(browser.back())   # Canot go back

print(browser.forward()) # Going forward to: https://www.youtube.com/
print(browser.forward()) # Going forward to: https://stackoverflow.com/questions
print(browser.forward()) # Cannot go forward.


        
        
        

