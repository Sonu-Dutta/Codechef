# Write a program to find the factorial value of any number entered by the user.
# Input
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains an integer N.

# Output
# For each test case, display the factorial of the given number N in a new line.

# Input
# 3 
# 3 
# 4
# 5

# Output

# 6
# 24
# 120

from math import factorial

for i in range(int(input("Enter number of test cases: "))):
    x = int(input("Enter number: "))
    
    print(factorial(x))