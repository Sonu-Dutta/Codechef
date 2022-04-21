t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    
    # print(a)
    x=a[0]
    y=a[1]
    z=a[2]
    
    b=y/x
    
    c=z-b
    if c>0:
        print(int(c))
    else:
        print(0)    