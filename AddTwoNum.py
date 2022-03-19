# Shivam is the youngest programmer in the world, he is just 12 years old. 
# Shivam is learning programming and today he is writing his first program.
# The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

N = int(input("How many times you want to perform addition ?"))
while N > 0:
    x, y = map(int, input("Enter two numbers with a space in between :").split())
    sum = x + y
    print(x ," + ",y," = ",sum)
    N = N - 1