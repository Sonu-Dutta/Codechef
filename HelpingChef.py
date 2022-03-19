
# Write a program, which takes an integer N and if the number is less than 10 then display "Thanks for helping Chef!" otherwise print "-1".

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, output the given string or -1 depending on conditions, in a new line.

# Example
# Input
# 3 
# 1
# 12
# -5
# Output
# Thanks for helping Chef!
# -1
# Thanks for helping Chef!

t=int(input("Enter number of test cases: "))
for _ in range(t):
    n=int(input("Enter number: "))
    if n<10:
        print("Thanks for helping Chef!")
    else:
        print("-1")