t = int (input("Nhap thang:"))
if (t>=1 and t<=12):
    if (t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12):
        print("31 ngay")
    elif (t==4 or t==6 or t==9 or t==11):
        print("30 ngay")
    elif (t==2):
        print("28 hoac 29 ngay")
else:
    print ("INVALID")