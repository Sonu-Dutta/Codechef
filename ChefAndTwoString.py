
for _ in range(int(input("Enter number of test cases: "))):
    s1 = input("Enter 1st string: ")
    s2 = input("Enter 2nd string: ")
    
    min_cnt = 0
    max_cnt = 0
    
    for i in range(len(s1)):
        if s1[i] == '?' or s2[i] == '?':
            max_cnt += 1
        elif s1[i] != s2[i]:
            min_cnt += 1
            max_cnt += 1
    print(min_cnt, max_cnt)