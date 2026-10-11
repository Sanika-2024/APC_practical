def palindrome(s):
    if s == s[::-1]:
        print("Is Palindrome")
    else:
        print("Is not palindrome")

def count_vowel(s):
    count=0
    for ch in s.lower():
        if ch in 'aeiou':
            count += 1
    print("Vowel count:",count)
    
def char_frequency(s):
    ch=input("Enter a Character")
    print("Frequency:",s.count(ch))
        
    
    
    
