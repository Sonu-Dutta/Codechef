# While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 1000.
# If the quantity and price per item are input, write a program to calculate the total expenses.

# Input

# 3 
# 100 120
# 10 20
# 1200 20

# Output

# 12000.000000
# 200.000000
# 21600.000000

t = int(input("Enter number of test cases: "))
for i in range(t):
    q,p = map(int, input("Enter quantity and price : ").split())
    m = q*p
    if (q > 1000):
        m = m - m*(0.1)
    else:
        m = m
    print(format((m),".6f"))