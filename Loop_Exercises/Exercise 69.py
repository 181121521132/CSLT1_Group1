pi=0
for term in range (15): 
    if term==0:
        pi=pi+3
    else:
        sign=(-1)**(term+1)
        x=2*term
        denominator=(x)*(x+1)*(x+2)
        pi=pi+((sign)*(4/denominator))
    print(pi)