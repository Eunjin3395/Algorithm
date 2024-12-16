import heapq

def solution(n, costs):
    # 인접 리스트 생성
    adj_list = [[] for _ in range(n)]
    for x, y, cost in costs:
        adj_list[x].append((cost, y))
        adj_list[y].append((cost, x))

    # 방문 여부를 확인하는 배열
    visited = [False] * n
    
    # 우선순위 큐(힙)에 시작 노드를 추가 (0번 섬에서 시작)
    pq = [(0, 0)]  # (비용, 노드)
    total_cost = 0
    
    while pq:
        cost, node = heapq.heappop(pq)
        
        if visited[node]:
            continue
        
        # 방문 처리하고 비용을 누적
        visited[node] = True
        total_cost += cost
        
        # 인접 노드 중 방문하지 않은 노드를 우선순위 큐에 추가
        for next_cost, next_node in adj_list[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_cost, next_node))
    
    return total_cost