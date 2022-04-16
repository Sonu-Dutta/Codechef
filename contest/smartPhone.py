lst=[]
lst2=[]
t=int(input())
for i in range(t):
    n=int(input())
    lst.append(n)
# print(lst)    
lst.sort()
s=t

for i in range(t):
    v=lst[i]*s
    print(lst[i],s)
    s-=1
    lst2.append(v)
print(max(lst2))