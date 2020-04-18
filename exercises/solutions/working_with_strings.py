"""
 The exercises below will get you more comfortable working with 
 strings, string methods, and operations.

 Reference: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
"""

# 1. Print 'Hello World' - Use single quotes
print('Hello World')

# 2. Print "Hello World" - Use double quotes
print("Hello World")

# 3. Print "Hello World" - Use three single quotes
print('''Hello World''')

# 4. Print "Hello" "World" on separate lines (use the newline character)
print("Hello\n\tWorld using new line character ") # \t is the tab character

# 5. Using string methods, print "Hello World" all lowercase
print("Hello World".lower())

# 6. Using string methods, print "Hello World" all uppercase
print("Hello World".upper())

# 7. Using string methods, check if all characters in the string "It is 8:00am"
#    are alphabetic and there is at least one character
print("It is 8:00am".isalpha())

# 8. Using string methods, check if all characters in the string "8675309"
#    are digits and there is at least one character
print("8675309".isdigit())

# 9. Using an operator, combine the strings "Hello" and "World"
print("Hello " + "World" + " using string concatentation (addition) ") # concatenation

# 10. Using the print function alone (no string methods, no operators), , combine the strings "Hello" and "World"
#     see: https://docs.python.org/3/library/functions.html#print
print("Hello ", "World using multiple arguments to the print function")

# 11. Remove the "***" characters in the following string: "***SUCCESS"
print("***SUCCESS using 'replace' string method".replace("***", ''))
print("***SUCCESS using 'lstrip' string method".lstrip("***"))
print("***SUCCESS using 'strip' string method".strip('*'))

# 12. What is the zero index in the following string: "Make sure to use brackets!"
print("Make sure to use brackets!"[0])

# 13. What is the length of the following string: "Make sure to use brackets!"
print(len("Make sure to use brackets!"))