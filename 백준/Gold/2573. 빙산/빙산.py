import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# 빙산이 있는 좌표만 저장 (초기화)
icebergs = deque()
for y in range(N):
    for x in range(M):
        if matrix[y][x] > 0:
            icebergs.append((y, x))

def decrease():
    """빙산이 녹는 과정 (빙산이 있는 좌표만 갱신)"""
    global matrix
    melting = {}  # 빙산이 얼마나 줄어들지를 저장하는 딕셔너리

    for _ in range(len(icebergs)):
        y, x = icebergs.popleft()
        count = 0  # 녹는 양

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 0:
                count += 1

        if count > 0:
            melting[(y, x)] = count
        else:
            icebergs.append((y, x))  # 녹지 않는다면 다시 큐에 추가

    # 실제 빙산 녹이기
    for (y, x), melt in melting.items():
        matrix[y][x] -= melt
        if matrix[y][x] <= 0:
            matrix[y][x] = 0  # 빙산이 녹아 없어짐
        else:
            icebergs.append((y, x))  # 아직 남아있다면 다시 큐에 추가

def bfs(y, x, visited):
    """BFS로 빙산 덩어리 탐색"""
    queue = deque([(y, x)])
    visited[y][x] = True

    while queue:
        cy, cx = queue.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and matrix[ny][nx] > 0:
                visited[ny][nx] = True
                queue.append((ny, nx))

years = 0
while icebergs:
    decrease()
    
    # 빙산 덩어리 개수 확인
    visited = [[False] * M for _ in range(N)]
    count = 0

    for y, x in icebergs:
        if not visited[y][x] and matrix[y][x] > 0:
            bfs(y, x, visited)
            count += 1
            if count >= 2:  # 두 덩어리 이상이면 즉시 종료
                print(years + 1)
                exit(0)

    years += 1  # 1년 경과

print(0)  # 다 녹았는데도 분리되지 않으면 0 출력
