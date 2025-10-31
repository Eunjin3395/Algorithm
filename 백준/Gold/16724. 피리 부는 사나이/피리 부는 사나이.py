import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
safe_zone = 0

# 방향 매핑
dir_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def dfs(y, x, mark):
    visited[y][x] = mark
    dy, dx = dir_map[graph[y][x]]
    ny, nx = y + dy, x + dx

    if not visited[ny][nx]:
        dfs(ny, nx, mark)
    elif visited[ny][nx] == mark:
        # 같은 그룹 내에서 다시 돌아온 경우 → 사이클 발견
        global safe_zone
        safe_zone += 1

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i, j, i*m + j + 1)  # 각 탐색마다 고유 마킹값

print(safe_zone)
