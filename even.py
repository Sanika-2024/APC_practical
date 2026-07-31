n = int(input("Enter the value of n: "))

print(f"Even numbers up to {n}:")
# Starts at 2, increments by 2 each step
for i in range(2, n + 1, 2):
    print(i, end=" ")
