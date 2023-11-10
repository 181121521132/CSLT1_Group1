a=int(input("Nhap muc am luong:"))
if (a>0 and a<40):
    print ("muc am luong yen tinh hon can phong yen tinh")
elif (a==40):
    print("muc am luong nhu can phong yen tinh")
elif (a>40 and a<70):
    print ("muc am luong yen tinh hon bao thuc")
elif (a==70):
    print("muc am luong nhu bao thuc")
elif (a>70 and a<106):
    print("muc am luong yen tinh hon may cat co")
elif (a==106):
    print("muc am luong nhu may cat co")
elif (a>106 and a<130):
    print ("muc am luong yen tinh hon tieng bua khoan ")
elif (a==130):
    print("muc am luong nhu tieng bua khoan")
elif (a>130):
    print("muc am luong qua on ao")
else:
    print("INVALID")