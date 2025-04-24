class TaiKhoan:
    def __init__(self, stk, ten, so_du = 0  ):
        self.stk = stk
        self.ten = ten 
        self.so_du = so_du 

    def rut_tien(self, so_tien):
        if so_tien > self.so_du:
            print(f"Không đủ tiền trong tài khoản {self.stk} để rút {so_tien}VNĐ")
        else:
            self.so_du -= so_tien
            print(f"Đã rút {so_tien}VNĐ từ tài khoản {self.stk}. Số dư còn lại: {self.so_du}VNĐ")
        
    def nap_tien(self, so_tien):
        self.so_du += so_tien
        print(f"Đã nạp {so_tien}VNĐ vào tài khoản {self.stk}. Số dư mới: {self.so_du}VNĐ")
        
    def lay_so_du(self):
        return self.so_du

class TaiKhoanTietKiem(TaiKhoan):
    def __init__(self, stk, ten, so_du = 0, lai_suat = 0.05):
        super().__init__(stk, ten, so_du)
        self.lai_suat = lai_suat

    def tinh_lai_suat(self):
        tien_lai = self.so_du * self.lai_suat
        self.so_du += tien_lai
        print(f'Đã cộng lãi {tien_lai:.0f}VNĐ vào tài khoản {self.stk}. Số dư mới: {self.so_du}VNĐ')
        

def main():
    tk1 = TaiKhoan("001", "Ngo Chi Kien", 1000000)
    tk2 = TaiKhoanTietKiem("002", "Nguyen Linh", 2000000, 0.07)

    # Thực hiện các thao tác
    tk1.nap_tien(500000)
    tk1.rut_tien(300000)
    tk1.rut_tien(2000000)  

    tk2.rut_tien(500000)
    tk2.tinh_lai_suat()
    tk2.nap_tien(1000000)

    # In số dư cuối cùng
    print(f"Số dư tài khoản {tk1.stk} của {tk1.ten}: {tk1.lay_so_du()}đ")
    print(f"Số dư tài khoản tiết kiệm {tk2.stk} của {tk2.ten}: {tk2.lay_so_du():.0f}đ")


if __name__ == "__main__":
    main()




