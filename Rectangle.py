
# You are given four integers a, b, c and d. Determine if there's a rectangle such that the lengths of its sides are a, b, c and d (in any order).

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains four space-separated integers a, b, c and d.
# Output
# For each test case, print a single line containing one string "YES" or "NO".

# Sample Input 1 
# 3
# 1 1 2 2
# 3 2 2 3
# 1 2 2 2
# Sample Output 1 
# YES
# YES
# NO

T=int(input("Enter number of test cases: "))
for j in range(T):
    a,b,c,d = input("Enter lengths of rectangle: ").split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if((a==b and c==d) or (a==c and b==d) or (a==d and b==c)):
        print("YES")
    else:
        print("NO")