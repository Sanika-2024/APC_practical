n = int(input("Enter n value: "))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n, 0, -1):
    print(" ".join(letters[:i]))
