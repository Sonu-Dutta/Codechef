# If Give an integer N . Write a program to obtain the sum of the first and last digits of this number
#Solution Provided by CodingBroz 
T = int(input("Enter number of test cases: "))
while T > 0:
    n = (input("Enter number: "))
    reverse = n[::-1]
    print(reverse)
    reverse = int(reverse)
    n = int(n)
    first_digit = reverse % 10
    last_digit = n % 10
    sum = first_digit + last_digit
    print(sum)
    T = T - 1