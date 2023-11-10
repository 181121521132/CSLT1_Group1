#Input: Nhap vao chu cai
#Output: Tra ve là "nguyen am" neu nhap a, e, i, o hoac u
#Tra ve "Doi khi la nguyen am hoac doi khi la phu am" neu nhap y
#Tra ve la "Phu am" voi cac truong hop con lai

text = input("Nhap vao vao chu cai: ")

if text in ('a', 'e', 'i', 'o', 'u'):
    print("Chu da nhap", text, "la nguyen am")
elif text == 'y':
    print("Thỉnh thoảng y la nguyen am, thinh thoang y la phu am")
else:
    print("Chu da nhap", text, "la phu am")