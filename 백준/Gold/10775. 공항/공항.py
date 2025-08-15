import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

G = int(input())
P = int(input())

# G*P 완탐 불가

# 각각의 비행기 도킹마다 최대한 주어진 g에 가까운 게이트에 내리는게 이득임
# 최대한 가까운 도킹 가능한 게이트 구하기
# 이미 도킹된 게이트끼리 집합으로 연결
# 주어진 g가 visited이면 g가 속한 집합의 root 노드 찾고 root-1 게이트에 도킹
# visited 아니면 g를 visited 처리하고, g+1과 union, g-1과 union (g+1,g-1이 visited인 경우)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(G + 1)]
visited = set()
answer = 0

for _ in range(P):
    g = int(input())

    if g not in visited:
        visited.add(g)
        # print("도킹:", g)

        # g+1이 도킹된 경우
        if g + 1 in visited:
            union(g, g + 1)

        # g-1이 도킹된 경우
        if g - 1 in visited:
            union(g, g - 1)
        # print(parent)
    else:
        root = find(g)
        if root - 1 >= 1 and root - 1 not in visited:
            # print("도킹:", root - 1)
            # root-1과 g union
            visited.add(root - 1)
            union(root - 1, g)

            if root - 2 >= 1 and root - 2 in visited:
                union(root - 2, root - 1)  # root-2와 root-1 union

            # print(parent)
        else:
            print(answer)
            exit()  # 공항 폐쇄
    answer += 1
    # print("visited:", visited)

print(answer)
