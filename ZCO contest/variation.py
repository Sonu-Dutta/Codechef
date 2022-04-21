N, K = map(int, input().split())
numberList = list(map(int, input().split()))
numberList.sort()
answer = 0
i,j = 0,1

while(j<N):
    if numberList[j] - numberList[i] >= K :
        i += 1
        answer += N - j
    else :
        j += 1
print(answer)