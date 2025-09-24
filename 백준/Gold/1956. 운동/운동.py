import sys
input = sys.stdin.readline

V, E = map(int, input().split())
INF = 1e9
graph = [[INF] * (V + 1) for _ in range(V + 1)]

# 플로이드 워셜
# 입력받아 가중치 초기화
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식
for mid in range(1, V + 1):
    for start in range(1, V + 1):
        for end in range(1, V + 1):
            if graph[start][mid] == INF or graph[mid][end] == INF:
                continue
            graph[start][end] = min(graph[start][end], graph[start][mid] + graph[mid][end])


answer = INF
for i in range(1, V + 1):
    answer = min(answer, graph[i][i])  # 자기 자신으로 돌아오는 최단 경로

print(answer if answer < INF else -1)
