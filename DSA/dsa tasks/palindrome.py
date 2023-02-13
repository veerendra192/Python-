def palindrome(string):
    return string == string[::-1]

string = input("Enter string: ").strip()

if palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
