import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def dfs(x):
    global count
    visited[x] = True
    path.append(x)
    next = graph[x]

    if not visited[next]:
        dfs(next)
    else:
        if not finished[next]:
            # 사이클 발견 → next부터 현재 x까지가 사이클
            cycle_idx = path.index(next)
            count -= len(path[cycle_idx:])  # 사이클에 포함된 애들 제외

    finished[x] = True
    path.pop()

for _ in range(T):
    n = int(input())
    data = list(map(int, input().split()))
    graph = [0] + data  # 1-indexed
    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    count = n
    path = []

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(count)