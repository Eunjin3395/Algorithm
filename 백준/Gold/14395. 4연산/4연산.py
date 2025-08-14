from collections import deque
from collections import defaultdict
import sys

S, T = map(int, input().split())

if S == T:
    print(0)
    exit()

# 백트래킹으로 될까??
# 아니다 최소 연산횟수니까 bfs 최단경로처럼 가능할지?

q = deque()
visited = defaultdict(lambda: False)  # 기본 value를 False로 갖는 dict

q.append((S, ""))  # node, calc
visited[S] = True

while q:
    node, calc = q.popleft()

    if node > 10e9:
        continue

    if node == T:
        print(calc)
        quit()

    nxt = node**2
    if not visited[nxt]:
        q.append((nxt, calc + "*"))
        visited[nxt] = True

    nxt = node * 2
    if not visited[nxt]:
        q.append((nxt, calc + "+"))
        visited[nxt] = True

    if len(calc) == 0:  # 첫 depth에서
        q.append((0, "-"))
        q.append((1, "/"))
        visited[0] = True
        visited[1] = True

print(-1)
