import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

A, B = map(int, input().split())
dijkstra(A)
print(distance[B])
 