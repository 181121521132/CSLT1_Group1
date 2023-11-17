n=int(input("n="))
m=int(input("m="))
d=min(n,m)
while n%d!=0 or m%d!=0:
    d=d-1
print("Uoc chung lon nhat cua",n, "va", m, "la:", d)