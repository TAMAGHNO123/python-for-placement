def find_fact(x):
    
    if x < 0:
        print("Entered number is not valid...")
        return None
        
    total = 1   #will be used to accumulate the factorials
    for i in range(1, x+1):
        total = total*i
        
    return total

u = int(input("Enter a number to get its factorial : "))

print("Factorial is : ", find_fact(u))