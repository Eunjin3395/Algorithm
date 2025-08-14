import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 특정 노드가 속한 집합의 루트 노드 찾기
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# a,b노드가 속한 집합 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

# 부모 리스트 초기화
parent = [0] * (N + 1)
for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    cmd, a, b = map(int, input().split())
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
