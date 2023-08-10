import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v]=True
    print(v,end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque([start])

    visited[start]=True

    while(queue):
        v = queue.popleft()
        print(v,end=" ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


N,M,V = map(int,sys.stdin.readline().rstrip().split())
graph = [ [] for _ in range(N+1) ]
graph[0]=[]
visited_dfs=[False]*(N+1)
visited_bfs=[False]*(N+1)

for i in range(M):
    v1,v2 = map(int,sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for elem in graph:
    elem.sort();

dfs(graph,V,visited_dfs)
print()
bfs(graph,V,visited_bfs)