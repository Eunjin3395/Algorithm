import sys
import copy
input = sys.stdin.readline
INF = int(1e9)

# 플로이드 워셜의 dist 행렬 출력하는 문제
N = int(input())
M = int(input())
adj_matrix = [[INF] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    adj_matrix[a - 1][b - 1] = min(adj_matrix[a - 1][b - 1], c)

# dist 행렬 초기화
dist = copy.deepcopy(adj_matrix)
for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0

# 플로이드 워셜
for mid in range(N):
    for start in range(N):
        for end in range(N):
            if dist[start][mid] == INF or dist[mid][end] == INF:
                continue
            dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])

for row in dist:
    for elem in row:
        if elem == INF:
            print(0, end=" ")
        else:
            print(elem, end=" ")
    print()
