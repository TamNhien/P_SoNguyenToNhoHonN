def is_prime(num):
    # Kiểm tra nếu số là 2 hoặc nhỏ hơn 2 thì không phải số nguyên tố
    if num < 2:
        return False
    # Sử dụng biểu thức generator và hàm all để kiểm tra tính nguyên tố của số
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def main():
    # Nhập số nguyên dương n từ người dùng
    n = int(input("Nhap so nguyen duong n: "))
    # In ra thông báo
    print("Cac so nguyen to nho hon", n, "la : ", end=" ")
    # Sử dụng biểu thức generator để tạo ra danh sách các số nguyên tố nhỏ hơn n và in ra chúng
    print(*[i for i in range(2, n) if is_prime(i)], sep=", ")

if __name__ == "__main__":
    main()

def is_prime(num):
    if num < 2:
        return False
    return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

def main():
    