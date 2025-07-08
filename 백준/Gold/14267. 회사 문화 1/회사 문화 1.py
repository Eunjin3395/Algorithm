from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 상사의 번호는 자신의 번호보다 작다
# dp
# dp[i] = dp[arr[i]]+w, i가 받은 칭찬 크기 = i의 상사가 받은 칭찬 + i 본인이 받은 칭찬

dp = [0] * (N + 1)
dp[1] = 0
for _ in range(M):
    i, w = map(int, input().split())
    dp[i] += w

for i in range(2, N + 1):
    dp[i] += dp[arr[i - 1]]

print(*dp[1:])
