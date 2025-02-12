import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))


q = deque()
for i in range(N):
    while q and q[-1][1] > A[i]:  # 최솟값 갱신
        q.pop()

    q.append((i+1, A[i]))

    if q[-1][0] - q[0][0] >= L:  # 구간 크기 갱신
        q.popleft()

    print(q[0][1], end=" ")
