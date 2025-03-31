import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a]


def dfs(v):
    for nx in sorted(graph[v],reverse=True):
        if visited[nx] == -1:
            visited[nx] = visited[v]+1
            dfs(nx)
visited[r] = 0
dfs(r)

for i in range(1, n + 1):
    print(visited[i])