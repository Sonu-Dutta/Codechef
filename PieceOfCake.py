
# This is a very easy warm-up problem.
# You are given a string. Your task is to determine whether number of occurrences of some character in the string is equal to the sum of the numbers of occurrences of other characters in the string. 
# Input
# The first line of the input contains an integer T denoting the number of test cases. Each of the next T lines contains one string S consisting of lowercase latin letters.
# Output
# For each test case, output a single line containing "YES" if the string satisfies the condition given above or "NO" otherwise.
# Example
# Input:
# 4
# acab
# zzqzqq
# abc
# kklkwwww
# Output:
# YES
# YES
# NO
# YES

for i in range(int(input("Enter number of test cases: "))):
    a=input("Enter the string: ")
    d={}
    for j in a:
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
    k="NO"
    for j in d:
        if d[j]*2==len(a):
            k="YES"
            break
    print(k)
    
    
#     t=int(input())
# for _ in range(t):
#   n=input()
#   l=list(n)
#   m=[]
#   c=[]
#   for i in l:
#     if i not in m:
#       m.append(i)
#     j=0
#   while (j<len(m)):
#     c.append(l.count(m[j]))
#     j+=1
#     c.sort()
#   if (sum(c)/2==c[len(c)-1]):
#     print('YES')
#   else:
#     print ('NO')