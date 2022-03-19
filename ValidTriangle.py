
# Write a program to check whether a triangle is valid or not, when the three angles of the triangle are the inputs. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
# Input
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three angles A, B and C, of the triangle separated by space.
# Output
# For each test case, display 'YES' if the triangle is valid, and 'NO', if it is not, in a new line.

# Input
# 3 
# 40 40 100
# 45 45 90
# 180 1 1
# Output
# YES
# YES
# NO

for _ in range(int(input("Enter number of test cases: "))):
    a,b,c=map(int,input("Enter 3 angles of the triangle: ").split())
    if(a+b+c)==180:
        print("YES")
    else:
        print("NO")