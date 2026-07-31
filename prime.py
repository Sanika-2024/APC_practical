num = int(input("Enter a number: "))


root_float = num ** 0.5


if root_float % 1 == 0 and root_float > 1:
    root = int(root_float)
    divisors = 0
    
    
    for i in range(1, root + 1):
        if root % i == 0:
            divisors = divisors + 1
            
    if divisors == 2:
        print("The square root is prime.")
    else:
        print("The square root is not prime.")
else:
    print("Not a perfect square or less than 2.")
