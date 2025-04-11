## chữa bài 4

class DateHandler():
    def __init__(self): ## hàm khởi tạo 
        pass
    
    ## Class method
    def format_date(time):
        return time.strftime("%d/%m/%Y")
    
    ## Class method 2
    def get_days_between(time_start, time_end):
        return (time_end - time_start).days
    
from datetime import datetime # nhúng class datetime có sẵn trong python
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 1, 1)

print("Start: ", DateHandler.format_date(start_date))
print("End: ", DateHandler.format_date(end_date))
print("Days between: ", DateHandler.get_days_between(start_date, end_date))

        