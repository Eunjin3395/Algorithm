visited = []
adj_list=[]
cnt=0

def dfs(node):
    global adj_list, visited, cnt
    if visited[node]:
        return
    visited[node] = True
    cnt+=1
    for next_node in adj_list[node]:
        dfs(next_node)

def solution(n, wires):
    global visited, adj_list, cnt
    adj_list=[[] for _ in range(n+1)]
    for wire in wires:
        adj_list[wire[0]].append(wire[1])
        adj_list[wire[1]].append(wire[0])
        
    diff_arr = []
    
    # 모든 전선 탐색
    for i in range(n-1):
        # 전선 하나 제거
        remove_wire = wires[i]
        adj_list[remove_wire[0]].remove(remove_wire[1])
        adj_list[remove_wire[1]].remove(remove_wire[0])
        
        # 노드 탐색 후 두 전력망의 송전탑 개수 arr에 저장
        visited = [False]*(n+1)
        cnt = 0
        arr = []
        for node in range(1,n+1):
            if not visited[node]:
                dfs(node)
                arr.append(cnt)
                cnt=0
        
        # 두 전력망의 송전탑 개수 차이 diff_arr에 저장
        diff = abs(arr[0]-arr[1])
        diff_arr.append(diff)
        
        # 제거했던 전선 복구
        adj_list[remove_wire[0]].append(remove_wire[1])
        adj_list[remove_wire[1]].append(remove_wire[0])
        
    return min(diff_arr)