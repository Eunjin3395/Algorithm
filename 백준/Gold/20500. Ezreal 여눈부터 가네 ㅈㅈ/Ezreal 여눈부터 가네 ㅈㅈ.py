N = int(input())
MOD = 1000000007
dp = [[0 for _ in range(3)] for _ in range(N + 1)]
dp[1][1] = 1

for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1] + dp[i - 1][2]
    dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1]

print(dp[N][0] % MOD)
