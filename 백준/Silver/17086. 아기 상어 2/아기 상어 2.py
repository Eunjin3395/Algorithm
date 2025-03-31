from collections import deque

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0, -1, -1, 1, 1]
dx = [0, 1, 0, -1, -1, 1, -1, 1]

# 거리 저장 배열
dist = [[-1] * M for _ in range(N)]
q = deque()

# 1인 위치를 모두 큐에 넣고, 거리 0으로 설정
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0

# BFS 시작
while q:
    y, x = q.popleft()

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

# 0 위치들의 거리 중 최댓값 출력
answer = 0
for i in range(N):
    for j in range(M):
        answer = max(answer, dist[i][j])

print(answer)