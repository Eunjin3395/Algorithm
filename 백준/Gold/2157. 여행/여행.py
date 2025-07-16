import heapq
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# dp? 그래프탐색?
# 도시 번호가 증가하는 순서대로만 이동한다
# 그냥 dp로 다시 풀기

adj_list = [[] for _ in range((N + 1))]
for _ in range(K):
    a, b, c = map(int, input().split())
    if a < b:
        adj_list[a].append((b, c))

# dp[i][j]: i번 도시에 도착했고 그동안 j개를 골라서 방문했을 때의 최대 만족도
dp = [[-1] * (M + 1) for _ in range(N + 1)]
dp[1][1] = 0

for i in range(1, N + 1):
    for j in range(1, M):
        if dp[i][j] == -1:  # 해당 도시 방문하지 않은 경우
            continue

        for nxt, cost in adj_list[i]:
            dp[nxt][j + 1] = max(dp[nxt][j + 1], dp[i][j] + cost)

print(max(dp[N][2:]))

