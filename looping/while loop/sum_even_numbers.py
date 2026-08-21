n = int(input("Enter n: "))
sum_even = sum(i for i in range(2, n + 1, 2))
print("Sum of even numbers up to", n, "=", sum_even)