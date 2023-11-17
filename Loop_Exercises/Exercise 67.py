tong_tien = 0.00
while True:
    a = input("Tuoi=")

    if a == "":
        break
    a = int(a)
    if 0<= a <= 2:
        tien = 0.00
    elif 3 <= a <= 12:
        tien = 14.00
    elif a >= 65:
        tien = 18.00
    else:
        tien = 23.00
    tong_tien += tien
print("Tong tien:", tong_tien)
