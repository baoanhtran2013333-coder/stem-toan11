import math

def giai_phuong_trinh_luong_giac():
    print("\n--- GIẢI PHƯƠNG TRÌNH sin(x) = a ---")
    try:
        a = float(input("Nhập giá trị a (-1 <= a <= 1): "))
        if a < -1 or a > 1:
            print("Lỗi: Giá trị a phải nằm trong khoảng [-1, 1]!")
            return
        rad = math.asin(a)
        deg = math.degrees(rad)
        print(f"=> Nghiệm Radian: x = {rad:.4f} + k2π hoặc x = {math.pi - rad:.4f} + k2π (k ∈ Z)")
        print(f"=> Nghiệm Độ: x = {deg:.2f}° + k360° hoặc x = {180 - deg:.2f}° + k360° (k ∈ Z)")
    except ValueError:
        print("Vui lòng nhập số thực hợp lệ!")

def cap_so_cong():
    print("\n--- TÍNH CẤP SỐ CỘNG ---")
    try:
        u1 = float(input("Nhập số hạng đầu (u1): "))
        d = float(input("Nhập công sai (d): "))
        n = int(input("Nhập số hạng thứ n: "))
        un = u1 + (n - 1) * d
        sn = (n * (u1 + un)) / 2
        print(f"=> Số hạng thứ {n} (u_{n}) = {un}")
        print(f"=> Tổng {n} số hạng đầu (S_{n}) = {sn}")
    except ValueError:
        print("Dữ liệu không hợp lệ!")

def tinh_xac_suat():
    print("\n--- TÍNH XÁC SUẤT P(A) ---")
    try:
        nA = int(input("Nhập số kết quả thuận lợi n(A): "))
        nOmega = int(input("Nhập tổng số kết quả n(Ω): "))
        if nOmega <= 0 or nA < 0 or nA > nOmega:
            print("Lỗi dữ liệu!")
            return
        P = nA / nOmega
        print(f"=> Xác suất P(A) = {nA}/{nOmega} = {P:.4f} ({P*100:.2f}%)")
    except ValueError:
        print("Dữ liệu không hợp lệ!")

def main():
    while True:
        print("\n==========================================")
        print("   CHƯƠNG TRÌNH STEM TOÁN 11 - PYTHON     ")
        print("==========================================")
        print("1. Giải phương trình sin(x) = a")
        print("2. Tính Cấp số cộng")
        print("3. Tính Xác suất P(A)")
        print("0. Thoát")
        
        chon = input("Chọn chức năng (0-3): ")
        if chon == '1':
            giai_phuong_trinh_luong_giac()
        elif chon == '2':
            cap_so_cong()
        elif chon == '3':
            tinh_xac_suat()
        elif chon == '0':
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
