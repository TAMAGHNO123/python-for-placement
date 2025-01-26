'''
Understanding if not arr:
Falsy Values in Python:

An empty list ([]) is considered falsy.
Other falsy values include 0, None, False, empty strings (""), and empty tuples (()).


input("Enter the elements of the array separated by spaces: ")  -->This function prompts the user to enter a string of text. The message inside the parentheses is displayed to the user.

split()---> if the user inputs 1 2 3, split() will return the list ['1', '2', '3']

map(int, ...)----> The map() function applies the int function to each element of the list produced by split().
This converts each string in the list to an integer.
Continuing the previous example, map(int, ['1', '2', '3']) will produce an iterable of integers: 1, 2, 3.


list(map(int, ['1', '2', '3'])) -----> will produce the list [1, 2, 3]
'''
def largest_elm(nums):
    #check the array is empty or not
    if not nums:
        print("The given array is empty...")
        
    largest = nums[0]   #initialize first element as largest
    
    for i in nums:
        if  i > largest:
            largest = i
            
    return largest
        
        
#taking input from the user      
try:
    nums = list(map(int, input("Enter the elements separated by space : ").split()))
    print("The largest element is : ",largest_elm(nums))
except ValueError:
    print("Error!! Enter valid integers....")