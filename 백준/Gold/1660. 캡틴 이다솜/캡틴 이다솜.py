import sys
N = int(input())

size = [1]

# 사면체 크기 배열 채우기
layer = 1
dx = 1
while size[-1] < N:
    dx += 1  # layer 증가량
    layer += dx
    if size[-1] + layer > N:
        break
    size.append(size[-1] + layer)

# 사면체 크기 배열 길이 = 최대 121

# dp로 해야한다
# dp[i]: i개 대포알로 만들 수 있는 사면체 최소 개수

# dp 초기화
INF = sys.maxsize
dp = [INF] * (N + 1)
dp[0] = 1
for s in size:
    dp[s] = 1

# dp 배열 채우기
for i in range(2, N + 1):
    for s in size:  # 사면체 크기별 탐색
        if s > i:
            break
        dp[i] = min(dp[i], dp[i - s] + 1)

print(dp[N])
