t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    a1,b1,c1=map(int,input().split())
    n1=a+b+c
    n2=a1+b1+c1
        
    if(n1>n2):
        print("DRAGON")
    elif(n1<n2):
        print("SLOTH")
    elif(n1==n2):
        if(a>a1):
            print("DRAGON")
        elif(a1>a):
            print("SLOTH")
        elif(a==a1):
            if(b>b1):
                print("DRAGON")
            elif(b1>b):
                print("SLOTH")
                
            else:
                print("TIE")