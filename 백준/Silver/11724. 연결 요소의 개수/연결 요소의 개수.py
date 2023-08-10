import sys
sys.setrecursionlimit(5000)

def dfs(graph, v, visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

N,M = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v1,v2 = map(int,sys.stdin.readline().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False]* (N+1)

count=0

for i in range(1,N+1):
    if not visited[i]:
        if not graph[i]:
            count+=1
            visited[i]=True
        else:
            dfs(graph,i,visited)
            count+=1

print(count)