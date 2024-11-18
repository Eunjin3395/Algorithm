import sys
import heapq
input = sys.stdin.readline

INF = int(1e12)

# 입력 받기
n, m, r = map(int, input().split())  # 노드의 개수, 수색범위, 간선의 개수
items = [0] + list(map(int, input().split()))  # 각 노드의 아이템 개수

adj_list = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    adj_list[a].append([l, b])  # dist, node
    adj_list[b].append([l, a])

# print(adj_list)


def dijkstra(start):
    global m

    # print("==================dijkstra", start, "===================")

    dist = [INF]*(n+1)

    q = []
    heapq.heappush(q, [0, start])  # dist, node
    dist[start] = 0

    while q:
        curr_dist, curr_node = heapq.heappop(q)
        if dist[curr_node] < curr_dist:
            continue

        for adj_dist, adj_node in adj_list[curr_node]:
            temp_dist = curr_dist+adj_dist
            if temp_dist < dist[adj_node] and temp_dist <= m:
                dist[adj_node] = temp_dist
                heapq.heappush(q, [temp_dist, adj_node])
                # print("adj_node:", adj_node, "item_cnt:",
                #       item_cnt, "temp_dist:", temp_dist, ",m:", m)

    item_cnt = 0
    for i in range(1, n+1):
        if dist[i] <= m:
            item_cnt += items[i]

    return item_cnt


item_arr = []
for i in range(1, n+1):
    item_arr.append(dijkstra(i))

# print(item_arr)
print(max(item_arr))
