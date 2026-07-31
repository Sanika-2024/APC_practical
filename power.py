n = int(input("Enter the exponent limit (n): "))

print("The sequence is:")
# Loop from 0 up to n (inclusive)
for i in range(n + 1):
    term = 2 ** i
    print(term, end=" ")
