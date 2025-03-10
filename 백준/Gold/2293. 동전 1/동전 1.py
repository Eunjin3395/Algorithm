# 입력 받기
n, k = map(int, input().split())

values = [int(input()) for _ in range(n)]
values.sort()

dp = [0]*(k+1)
dp[0] = 1


for value in values:
    for i in range(value, k+1):
        dp[i] += dp[i-value]
# print(dp)

print(dp[k])
