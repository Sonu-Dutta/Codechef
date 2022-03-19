# Three numbers A, B and C are the inputs. Write a program to find second largest among them.
# Input
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.
# Output
# For each test case, display the second largest among A, B and C, in a new line.
# Input
# 3 
# 120 11 400
# 10213 312 10
# 10 3 450
# Output
# 120
# 312
# 10

N = int(input("Enter number of test cases : "))
for i in range(N):
    x = list(map(int, input("Enter number: ").split()))
    # print(x)
    x.sort()
    # print(x)
    print(x[-2])