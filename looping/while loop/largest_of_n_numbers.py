numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
if numbers:
    print("Largest number =", max(numbers))
else:
    print("No numbers were entered")