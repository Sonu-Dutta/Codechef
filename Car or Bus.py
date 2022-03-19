for i in range(int(input())):
    b,c=map(int,input().split())
    if (b>c):
        print("CAR")
    elif(c>b):
        print("BIKE")
    else:
        print("SAME")
