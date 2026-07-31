n = int(input("Enter the value of n: "))

total_sum = 1.0
factorial = 1


for i in range(1, n + 1):
    factorial *= i            
    total_sum += 1 / factorial  

print(f"The sum of the sequence is: {total_sum}")
