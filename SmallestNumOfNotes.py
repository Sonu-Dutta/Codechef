
# Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
# If the sum of Rs. N is input, write a program to computer smallest number of notes that will combine to give Rs. N.

# Input
# 3 
# 1200
# 500
# 242

# Output
# 12
# 5
# 7

T = int(input("Enter number of test cases: "))
a = [100, 50, 10, 5, 2, 1]
for i in range(T):
    n = int(input("Enter amount: "))
    b = 0
    for x in a:
        if (x <= n):
            b = b + (n // x )
            n = n % x
    print(b)        