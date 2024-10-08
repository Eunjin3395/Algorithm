from itertools import combinations
# 입력 받기
N = int(input())

S = [list(map(int, input().split())) for _ in range(N)]

arr = [i for i in range(0, N)]

# start팀이 될 N/2명의 조합 생성
minDiff = 9999999
for start in combinations(arr, N//2):
    link = [x for x in arr if x not in start]
    startPoint = 0
    linkPoint = 0
    for i in range(N):
        if arr[i] in start:
            for j in start:
                startPoint += S[i][j]
        else:
            for j in link:
                linkPoint += S[i][j]

    diff = abs(startPoint-linkPoint)

    if(diff < minDiff):
        minDiff = diff


print(minDiff)
