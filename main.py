"""
Fizz Buzz
=========

variable representing your maximum number

make a for loop that goes from 1 to your max number (including your max number)

print each number UNLESS the number is a multiple of 3 or 5

if the number is a multiple of 3 and not 5, print "fizz" instead of the number

if the number is a multiple of 5 and not 3, print "buzz" instead of the number

if the number is a multiple of both 3 and 5, print "fizzbuzz" instead of the number
"""


Maximum_Number = 15

for Number in range (1, Maximum_Number + 1):
    if Number % 3 == 0 and Number % 5 == 0:
        print ("Fizzbuzz")
    elif Number % 3 == 0:
        print ("Fizz")
    elif Number % 5 == 0:
        print ("Buzz")
    if Number % 3 != 0 and Number % 5 != 0:
        print (Number)