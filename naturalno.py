n = int(input("Enter the limit (N): "))

print(f"The first {n} natural numbers are:")

# Loop starts at 1 and stops at n (n + 1 is exclusive)
for i in range(1, n + 1):
    print(i, end=" ")
