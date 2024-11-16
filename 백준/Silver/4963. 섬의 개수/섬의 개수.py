import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(y, x):
    global matrix, visited

    if visited[y][x]:
        return

    visited[y][x] = True

    for i in range(-1, 2):
        for r in range(-1, 2):
            ny = i+y
            nx = r+x
            if ny == y and nx == x:
                continue

            if 0 <= ny < h and 0 <= nx < w:
                if matrix[ny][nx]:
                    dfs(ny, nx)


# 입력 받기
while(1):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        exit()

    matrix = [[] for _ in range(h)]

    for i in range(h):
        matrix[i] = list(map(int, input().split()))

    visited = [[False]*w for _ in range(h)]

    num = 0

    for y in range(h):
        for x in range(w):
            if not visited[y][x] and matrix[y][x]:
                num += 1
                dfs(y, x)

    print(num)
