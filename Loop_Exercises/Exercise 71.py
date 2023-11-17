x=float(input("x="))
guess = x/2
gioi_han = 1e-12
while abs(guess * guess - x) > gioi_han:
    guess =  (guess + x / guess) / 2
print ("Can bac 2 cua", x , "la =",guess, sep=" ")


