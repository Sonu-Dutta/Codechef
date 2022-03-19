#  You're given an integer N. Write a program to calculate the sum of all the digits of N.
n = int(input("How many times you want to perform this test ?\n "))
for _ in range(n):
    num = input("Enter a number: ")
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)