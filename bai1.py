# a)
name = input("Nhập tên của bạn: ")
print("Tên của bạn là: ", name)

#b)
n = len(name)
print(name, "có", n, "ký tự")
d = dict()
for i in range(1, n + 1):
    d[i] = i * i

print(d)