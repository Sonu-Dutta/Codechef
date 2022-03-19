# Given an Integer N, write a program to reverse it.
# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

for i in range(int(input("Enter number of test cases: "))):
    N = int(input("Enter number: "))
    Rev = 0
    while N > 0:
        Rev = Rev * 10 + N % 10
        N = N // 10
    print(Rev) 