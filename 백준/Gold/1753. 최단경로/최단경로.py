import heapq
import sys
input = sys.stdin.readline

# 입력 받기
V, E = map(int, input().split())
start_node = int(input())

adj_list = [[] for _ in range(V+1)]
INF = int(1e12)
dist = [INF] * (V+1)
dist[0] = 0

# 인접리스트 생성
for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append([w, v])  # dist, next_node

q = []
heapq.heappush(q, [0, start_node])  # q에 [dist,next_node] 추가
dist[start_node] = 0

while q:
    curr_dist, curr_node = heapq.heappop(q)
    # 탐색 최적화
    if dist[curr_node] < curr_dist:
        continue

    for adj_dist, adj_node in adj_list[curr_node]:
        temp_dist = curr_dist+adj_dist
        if(temp_dist < dist[adj_node]):
            dist[adj_node] = temp_dist
            heapq.heappush(q, [temp_dist, adj_node])


for elem in dist[1:]:
    if(elem == INF):
        print("INF")
    else:
        print(elem)
