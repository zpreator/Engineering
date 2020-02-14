"""
This function inputs a number and if
that number is less than 10 it prints the
value divided by 2. Afterward it prints
the number multiplied by 3
"""
def printValue1(num):
    if num < 10:
        print(num/2)
    print(3*num)

"""
This function inputs a number and if
that number is less than 0 it prints 0,
if it is not negative and less than 10 
it prints the value divided by 2.
"""
def printValue2(num):
    if num < 0:
        print(0)
    elif num < 10:
        print(num/2)
    

"""
This function inputs a number and if
that number is less than 0 it prints 0,
if it is not negative and less than 10 
it prints the value divided by 2, if the 
number is equal or greater than 10 it prints
the number divided by 3.
"""
def printValue3(num):
    if num < 0:
        print(0)
    elif num < 10:
        print(num/2)
    else:
        print(num/3)
    

"""
This function inputs a number and if
that number is less than 0 it prints 0,
if it is not negative, even, and less than 10 
it prints the value divided by 2, if the 
number is not negative, is odd, and less than 10
it prints the number divided by 3, if the
number is equal or greater than 10 and even
it prints the number divided by 4, if the
number is equal or greater than 10 and odd
it prints the number divided by 6.
"""
def printValue4(num):
    if num < 0:
        print(0)
    elif (num < 10) and (num%2 == 0):
        print(num/2)
    elif (num < 10) and (num%2 != 0):
        print(num/3)
    elif (num >= 10) and (num%2 == 0):
        print(num/4)
    else:
        print(num/6)
    

printValue4(11)