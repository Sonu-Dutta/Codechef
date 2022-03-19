
tests = int(input())
for _ in range(tests):
    N = int(input())
    l = [int(x) for x in input().split()]
    l.sort()
    min_g = l[-1] - l[0]
    for i in range(len(l)-1):
        min_l = l[i+1] - l[i]
        min_g = min(min_g, min_l)
    print(min_g)