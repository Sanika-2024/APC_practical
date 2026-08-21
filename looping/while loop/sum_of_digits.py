number = input("Enter a number: ")
sum_digits = sum(int(d) for d in number if d.isdigit())
print("Sum of digits =", sum_digits)