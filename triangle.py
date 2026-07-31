n = int(input("Enter n value: "))
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(1, n + 1):
    
    print(" ".join(letters[:i]))
