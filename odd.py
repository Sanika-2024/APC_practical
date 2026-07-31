n = int(input("Enter the value of n: "))

print(f"Odd numbers up to {n}:")
# Starts at 1, increments by 2 each step
for i in range(1, n + 1, 2):
    print(i, end=" ")
