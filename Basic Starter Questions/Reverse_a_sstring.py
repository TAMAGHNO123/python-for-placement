# Method using recursion
def reversing_using_recursion(s):
    if len(s) == 0:
        return s
    return s[-1] + reversing_using_recursion(s[:-1])


striing = input("Enter a string to reverse : ")
print("Reversed using recursion : ",reversing_using_recursion(striing))
        