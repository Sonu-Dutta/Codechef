#  Write a program to find the remainder when an integer A is divided by an integer B.
N = int(input("How many times you want to perform this test ?\n "))
while N > 0:
    a, b = map(int, input("Enter two numbers: ").split())
    Remainder = a % b 
    print(Remainder)
    N = N - 1