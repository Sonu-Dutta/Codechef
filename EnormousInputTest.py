# The purpose of this problem is to verify whether the method you are using to read input data is sufficiently fast to handle problems branded with the enormous Input/Output warning. 
# Input
# The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one positive integer ti, not greater than 109, each.

# Output
# Write a single integer to output, denoting how many integers ti are divisible by k.
# Example
# Input:
# 7 3
# 1
# 51
# 966369
# 7
# 9
# 999996
# 11

# Output:
# 4

N, K = map(int, input().split())
count = 0
while N > 0:
    a = int(input())
    if (a % K == 0):
        count += 1
    else:
        0
    N = N - 1
print(count)   