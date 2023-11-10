soCanh = int(input("So canh: "))
loaiHinh = ["Tam giac", "Tu giac", "Ngu giac", "Luc giac", "That giac", "Bat giac", "Cuu giac", "Thap giac"]

if 3 <= soCanh <= 10:
    tenHinh = loaiHinh[soCanh - 3]
    print(tenHinh)

elif soCanh < 3:
    print("Nhap sai gia tri")
    
else:
    print("Nhap qua gia tri cho phep")
