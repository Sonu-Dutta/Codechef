n,h=map(int,input().split())
m=list(map(int,input().split()))
q=list(map(int,input().split()))
c=0
j=0
for i in range(len(q)):
    if q[i]==0:
        for k in range(len(m)):
            print(m[k],end=" ")
    if q[i]==1:
        if j>0:
            j-=1
    if q[i]==2:
        if j<(n-1):
            j+=1
    if q[i]==3:
        if m[j]>0 and c==0:
            m[j]=m[j]-1
            c=1
    if q[i]==4:
        if m[j]<h and c==1:
            m[j]+=1
            c=0 