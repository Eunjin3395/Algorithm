from collections import deque

adj_list = []
# 그래프 연결 요소의 개수 구하기
def bfs(n, start_node, visited):
    global adj_list
        
    q = deque()
    q.append(start_node)
    visited[start_node] = True
    
    while q:
        curr_node = q.popleft()
        
        for adj_node in adj_list[curr_node]:
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True
        
    
    return 0
    

def solution(n, computers):
    global adj_list
    
    # 인접리스트 초기화
    adj_list = [[] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i==j: 
                continue
            if computers[i][j] == 1:
                adj_list[i].append(j)
    print(adj_list)
    
    visited = [False]* n
    answer = 0

    for i in range(n):
        if not visited[i]:
            bfs(n,i,visited)
            answer+=1
    
    
    return answer