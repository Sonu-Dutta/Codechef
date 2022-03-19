# Chef loves to play with arrays by himself. Today, he has an array A consisting of N distinct integers.
# He wants to perform the following operation on his array A.
# Select a pair of adjacent integers and remove the larger one of these two. This decreases the array size by 1. 
# Cost of this operation will be equal to the smaller of them.
# Find out minimum sum of costs of operations needed to convert the array into a single element.

# Sample Input 1 
# 2
# 2
# 3 4
# 3
# 4 2 5
# Sample Output 1 
# 3
# 4
# Explanation
# Test 1 : Chef will make only 1 move: pick up both the elements (that is, 3 and 4), remove the larger one (4), incurring a cost equal to the smaller one (3).
T = int(input("Enter number of test cases: "))
for i in range(T):
    N = int(input("Enter size of array: "))
    A = list(map(int,input("Enter numbers: ").split()))
    ans = (N-1)*min(A)
    print(ans)