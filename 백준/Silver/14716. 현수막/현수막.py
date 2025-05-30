from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y+dy, x+dx
            if (0 <= Y < M) and (0 <= X < N) and graph[Y][X] == 1:
                q.append((Y, X))
                graph[Y][X] = 0

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
d = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)