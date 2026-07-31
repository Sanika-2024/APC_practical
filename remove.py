text = input("Enter a string: ")
no_spaces = ""

for char in text:
    if char != " ":
        no_spaces += char

print("String without spaces:", no_spaces)
