import sys
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [1] * (N + 1)
arr = [tuple(map(int, input().split())) for _ in range(M)]
arr.sort()

for a, b in arr:
    if graph[b] <= graph[a]:
        graph[b] = graph[a] + 1

print(*graph[1:])
