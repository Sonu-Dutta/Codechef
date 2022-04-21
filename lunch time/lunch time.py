t=int(input())
lst=[]
for i in range(t):
    a=int(input())
    lst.append(a)
# print(lst)

for i in lst:
    if (i>=1 and i<=4):
        print("YES")
    else:
        print("NO")
