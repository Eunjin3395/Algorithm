import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
adj_list = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    if a != N - 1 and A[a] == 1:
        continue
    if b != N - 1 and A[b] == 1:
        continue

    adj_list[a].append((b, t))
    adj_list[b].append((a, t))

# print(adj_list)

# 다익스트라
INF = int(1e12)
dist = [INF] * N
dist[0] = 0

q = []
heapq.heappush(q, (0, 0))  # dist, node

while q:
    curr_dist, curr_node = heapq.heappop(q)

    if dist[curr_node] < curr_dist:
        continue

    for adj_node, adj_dist in adj_list[curr_node]:
        temp_dist = adj_dist + curr_dist
        if temp_dist < dist[adj_node]:
            heapq.heappush(q, (temp_dist, adj_node))
            dist[adj_node] = temp_dist

if dist[-1] == INF:
    print(-1)
else:
    print(dist[-1])
