import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [0] * N
for i in range(N):
    parent[i] = i

matrix = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(i + 1, N):
        if matrix[i][j]:
            union(i, j)

plan = [int(x) - 1 for x in input().split()]

root = find(plan[0])
for p in plan:
    if root != find(p):
        print("NO")
        exit()

print("YES")
