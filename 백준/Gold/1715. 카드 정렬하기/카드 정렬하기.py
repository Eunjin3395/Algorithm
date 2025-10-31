import sys
import heapq
input = sys.stdin.readline

N = int(input())

q = []

for _ in range(N):
    x = int(input())
    heapq.heappush(q, x)

if N == 1:
    print(0)
    sys.exit()
answer = 0

while q:
    a = heapq.heappop(q)

    if not q:
        break

    b = heapq.heappop(q)

    answer += a + b

    heapq.heappush(q, a + b)

print(answer)
