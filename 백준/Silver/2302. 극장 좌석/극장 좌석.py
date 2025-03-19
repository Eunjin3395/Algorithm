n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]

# dp[i]: 좌석이 i개 있을 때의 경우의 수
dp = [1, 1] + [0] * (n - 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1
prev = 0

for v in vip:
    answer *= dp[v - prev - 1]
    prev = v

answer *= dp[n - prev]

print(answer)
