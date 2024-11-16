import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력 받기
N = int(input())

adj_list = [[] for _ in range(N+1)]

for _ in range(N-1):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)


def dfs(node):
    global adj_list, prev

    for adj_node in adj_list[node]:
        if prev[adj_node] == -1:
            prev[adj_node] = node
            dfs(adj_node)


prev = [-1]*(N+1)
dfs(1)

for x in range(2, N+1):
    print(prev[x])
