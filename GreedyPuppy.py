
T=int(input("Enter number of test cases: "))
for i in range(T):
    n,k=map(int,input("Enter (N) and (K): ").split())
    c=0
    for h in range(1,k+1):
        if(n%h)>c:
            c=n%h
    print(c)
   