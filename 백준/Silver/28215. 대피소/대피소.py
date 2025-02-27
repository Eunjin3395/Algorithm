from itertools import combinations

N, K = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(N)]

# 대피소 조합 생성 후 바로 탐색 (메모리 절약)
min_max_dist = float('inf')

for shelters in combinations(range(N), K):
    max_dist = 0  # 현재 조합에서 가장 먼 집과 대피소 거리

    for i in range(N):
        if i in shelters:  # 대피소로 선택된 집은 제외
            continue

        x, y = home[i]
        min_dist = float('inf')  # 현재 집에서 가장 가까운 대피소 거리

        for s in shelters:
            sx, sy = home[s]
            min_dist = min(min_dist, abs(sx - x) + abs(sy - y))

        max_dist = max(max_dist, min_dist)  # 가장 먼 거리 업데이트

    min_max_dist = min(min_max_dist, max_dist)  # 전체 조합 중 최소값 찾기

print(min_max_dist)