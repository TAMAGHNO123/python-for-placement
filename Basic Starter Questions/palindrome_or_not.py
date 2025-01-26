def palindrome(s):
    #clean the string
    s = ''.join(s.split()).lower()
    #comparing string with reverse
    return s == s[::-1]
string = input("Enter to check palindrome or not : ")
if palindrome(string):
    print(f"'{string}' is a palindrome")
else:
    print(f"'{string}' is not a palindrome")