"""
Assignment 1.2: Write a program which will find all such numbers which
are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both
included). The numbers obtained should be printed in a comma-separated 
sequence on a single line
"""


mynum = 2000            # Initializing the variable
while mynum <= 3200:    # While loop to iterate the code
    num1 = mynum % 7    # To get remainder by dividing number by 7
    num2 = mynum % 5    # To get remainder by dividing number by 5
    if num1==0:         # Check if number is divisible by 7
        if num2!=0:     # Check if number is multiple of 5
            print(mynum,',',end='')
    mynum = mynum + 1

