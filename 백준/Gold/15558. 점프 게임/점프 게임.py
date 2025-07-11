from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
left = list(input().strip())
right = list(input().strip())
matrix = [left, right]


# bfs
visited = [[False] * N for _ in range(2)]
q = deque()
q.append((0, 0, 0))  # left/right, n, time

dk = [[0, 0, 1], [0, 0, -1]]
dn = [[1, -1, K], [1, -1, K]]



while q:
    k, n, t = q.pop()
    # print("curr:", k, n, t)

    if n >= N:
        print("1")
        exit()

    for i in range(3):
        nk = k + dk[k][i]
        nn = n + dn[k][i]


        if 0 <= nk <= 1 and 0 <= nn:
            # print("next node:", nk, nn, t + 1)
            if nn > t:
                if nn >= N:
                    print("1")
                    exit()

                if matrix[nk][nn] == "1" and not visited[nk][nn]:
                    # print("node append:", nk, nn, t + 1)
                    q.append((nk, nn, t + 1))
                    visited[nk][nn] = True

print("0")

