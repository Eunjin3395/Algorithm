N = int(input())

if N == 1:
    print(1)
    exit()

# 첫번째는 무조건 1
# 현재 숫자가 0이면 이전 숫자가 1 또는 0
# 현재 숫자가 1이면 이전 숫자가 0

# dp[a][b]: 현재 숫자가 a+1자리 이고, 숫자가 b일 때의 이친수의 개수
dp = [[0, 0] for _ in range(N)]
dp[0][1] = 1  # 1
dp[1][0] = 1  # 10

for i in range(2, N):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(dp[N-1][0]+dp[N-1][1])
