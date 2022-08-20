T = int(input())
for i in range(T):
    a, b, c, d, e = map(int, input().split())
    if (((a + b) <= d and c <= e) or ((b + c) <= d and a <= e) or ((a + c) <= d and b <= e)):
        print("Yes")
    else:
        print("No")
