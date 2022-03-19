# You are given a sequence a1, a2, ..., aN. Find the smallest possible value of ai + aj, where 1 ≤ i < j ≤ N.

# Example
# Input:
# 1
# 4
# 5 1 3 4

# Output:
# 4

# Explanation
# Here we pick a2 and a3. Their sum equals to 1 + 3 = 4.

T = int(input("Enter number of test cases: "))
for i in range(T):
    # n = int(input("Enter length of number: "))
    s = list(map(int, input("Enter numbers: ").split()))
    print(s)
    s.sort()
    print(s[0] + s[1])