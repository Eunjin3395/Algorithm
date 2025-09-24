import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N + 1)
adj_list = [[] for _ in range(N + 1)]


for _ in range(M):
    arr = list(map(int, input().split()))
    for k in range(1, arr[0]):
        adj_list[arr[k]].append(arr[k + 1])
        indegree[arr[k + 1]] += 1


q = deque()
answer = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    curr = q.popleft()
    answer.append(curr)

    for nxt in adj_list[curr]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

if len(answer) == N:
    print('\n'.join(map(str, answer)))
else:
    print(0)

