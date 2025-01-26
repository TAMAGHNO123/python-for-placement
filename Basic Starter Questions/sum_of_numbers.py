#using abs() allows the function to correctly compute the sum of the digits for any integer input, whether it is positive, negative, or zero.

def sum_of_numbers(number):
    number = abs(number)
    total = 0
    while number > 0 :
        total += number % 10
        number //= 10
        #dont put return here may cause indentation error
    return total
    
    
try:
    num = int(input("Enter a number : "))
    print("The sum of digits are : ",sum_of_numbers(num))
except ValueError:
    print("Please enter a valid number....")
    
    
    
    
    '''
    Modulus Operator (%)
Purpose: The modulus operator returns the remainder of the division of one number by another.
Usage: a % b gives the remainder when a is divided by b.
Example:
7 % 3 results in 1 because when you divide 7 by 3, the quotient is 2 and the remainder is 1.
10 % 2 results in 0 because 10 is evenly divisible by 2.





Floor Division Operator (//)
Purpose: The floor division operator divides one number by another and returns the largest integer that is less than or equal to the result (i.e., it discards the fractional part).
Usage: a // b gives the integer quotient of a divided by b.
Example:
7 // 3 results in 2 because 3 goes into 7 two times (with a remainder of 1).
10 // 3 results in 3 because 3 goes into 10 three times (with a remainder of 1).
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
