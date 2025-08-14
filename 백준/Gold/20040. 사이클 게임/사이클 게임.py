import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        print(m + 1)
        exit()

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    union(a, b)

print(0)

# 0-1-2-3
# 4-5

# 0-1-2
# \/
# 3
