for _ in range(int(input())):
     n,k=map(int,input().split())
     dict={}
     for x in input().split():
         dict.setdefault(x, 0)
     print(dict)
     for _ in range(k):
         s=input()
         for i in dict:
             if i in s:
                 dict[i]+=1
     print(dict)
     for i in dict:
         print("YES"*bool(dict[i]>0)+"NO"*bool(dict[i]==0),end=' ')
     print()