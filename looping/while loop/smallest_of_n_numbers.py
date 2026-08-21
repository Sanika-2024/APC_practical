numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
if numbers:
    print("Smallest number =", min(numbers))
else:
    print("No numbers were entered")