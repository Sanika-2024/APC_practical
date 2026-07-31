text = input("Enter a string: ")
target = input("Enter the character to count: ")

count = 0


for char in text:
    if char == target:
        count += 1

print(f"The character '{target}' appears {count} times.")
