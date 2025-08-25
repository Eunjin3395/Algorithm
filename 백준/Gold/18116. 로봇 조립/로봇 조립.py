import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())

parent = defaultdict(lambda: None)
size = defaultdict(lambda: 1)

def find(x):
    if parent[x] is None:
        parent[x] = x
        return x
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    parent[b] = a
    size[a] += size[b]

for _ in range(N):
    cmd = input().split()
    if cmd[0] == "I":
        a = int(cmd[1])
        b = int(cmd[2])
        union(a, b)
    else:
        c = int(cmd[1])
        root = find(c)
        print(size[root])