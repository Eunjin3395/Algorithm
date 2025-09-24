import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 1e9

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, v = map(int, input().split())
    adj_list[a].append((b, v))  # node, dist
    adj_list[b].append((a, v))


# 모든 노드에 대해 다익스트라 돌려서 dist 구하기
# dist 말고 경로도 구해야함

def dijkstra(start):
    pq = []
    dist = [INF] * (N + 1)

    heapq.heappush(pq, (0, start))  # dist, node
    dist[start] = 0

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if dist[curr_node] < curr_dist:
            continue

        for nxt, d in adj_list[curr_node]:
            temp_dist = curr_dist + d
            if temp_dist < dist[nxt]:
                heapq.heappush(pq, (temp_dist, nxt))
                dist[nxt] = temp_dist

                if curr_node == start:
                    route[start][nxt] = nxt
                else:
                    route[start][nxt] = route[start][curr_node]


route = [["-"] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dijkstra(i)

for y in range(1, N + 1):
    for x in range(1, N + 1):
        print(route[y][x], end=" ")
    print()
