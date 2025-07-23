import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

def is_connected(i, j):
    x1, y1, r1 = circles[i]
    x2, y2, r2 = circles[j]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2

T = int(input())
for _ in range(T):
    N = int(input())
    circles = [tuple(map(int, input().split())) for _ in range(N)]

    parent = list(range(N))

    for i in range(N):
        for j in range(i + 1, N):
            if is_connected(i, j):
                union(i, j)

    groups = set(find(i) for i in range(N))
    print(len(groups))