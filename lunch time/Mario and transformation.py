t=int(input())
l=["HUGE", "SMALL", "NORMAL"]
for i in range(t):
    n=int(input())
    d=n%3
    print(l[d-1])
    