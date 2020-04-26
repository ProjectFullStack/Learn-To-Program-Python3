"""
1. Write a function that prints the same thing twice, it will need one 
parameter (the value to print)
"""
def print_twice(string_to_print):
    print(string_to_print)
    print(string_to_print)
print_twice("I am inside a function!") # function call

"""
2. Write a function to square a number (multiply it by itself), it will only 
need one parameter (the number to square). The function should print the result.
"""
def square_number(number_to_square):
    print(number_to_square * number_to_square)
square_number(4) # function call

"""
3. Write a function to exponentiate a number, it will need two parameters. 
The function should print the result of the first parameter raised to 
the power of the second parameter.
"""
def exponentiate_number(number_to_raise, power):
    print(number_to_raise ** power)
exponentiate_number(4, 8) # function call