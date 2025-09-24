import sys
from collections import deque
input = sys.stdin.readline

# DAG위상정렬
# 각 depth마다 필요한 최대 시간의 합 구하기

def solve(W):
    dp = [0] * (N + 1)
    q = deque()

    for i in range(1, N + 1):
        if not indegree[i]:
            q.append(i)
            dp[i] = D[i]  # 시작 작업 소요 시간

    while q:
        node = q.popleft()

        for nxt in adj_list[node]:
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[node] + D[nxt])  # 이전 건물 중 가장 오래 걸리는 시간 + 자기 건설 시간

            if indegree[nxt] == 0:
                q.append(nxt)
    return dp[W]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))  # 1-based

    indegree = [0] * (N + 1)
    adj_list = [[] for _ in range(N + 1)]

    for _ in range(K):
        x, y = map(int, input().split())
        # x -> y
        adj_list[x].append(y)
        indegree[y] += 1

    W = int(input())

    print(solve(W))

