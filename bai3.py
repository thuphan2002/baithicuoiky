n = int(input("Nhập số nguyên dương n = "));
def isThuanNghich(n):
    str1 = str(n);  # ep kieu so n thanh chuoi
    str2 = str1[::-1];  # dao nguoc chuoi str1
    if (str1 == str2):
        return "là số thuận nghịch";
    else:
        return "không phải là số thuận nghịch";

print(n, isThuanNghich(n));

#a)
fullname = input("Nhập tên đầy đủ của bạn: ")
print("Tên đầy đủ của bạn là: ", fullname)

