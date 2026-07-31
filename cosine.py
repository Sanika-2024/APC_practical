x = float(input("Enter x: "))
n = int(input("Enter n (even number): "))

cos_sum = 1.0
term = 1.0


for i in range(2, n + 1, 2):
    term = term * (-x * x) / (i * (i - 1))
    cos_sum = cos_sum + term

print("Answer:", cos_sum)
