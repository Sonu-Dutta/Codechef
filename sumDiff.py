# Write a program to take two numbers as input and print their difference if the first number is greater than the second number otherwise print their sum.

# Input:
# First line will contain the first number (N1)
# Second line will contain the second number (N2)
# Output:
# Output a single line containing the difference of 2 numbers (N1−N2) if the first number is greater than the second number otherwise output their sum (N1+N2).

# Sample Input:
# 82
# 28
# Sample Output:
# 54

a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
if a > b:
    print( a - b )
else:
    print( a + b )