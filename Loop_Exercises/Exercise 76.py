n = int(input("Enter an integer (2 or greater): "))

if n < 2:
    print("n must be greater than 1")
else:
    factor = 2

    print("The prime factors of {n} are:")
    while factor <= n:
        if n % factor == 0:
            print(factor)
            n //= factor
        else:
            factor += 1
