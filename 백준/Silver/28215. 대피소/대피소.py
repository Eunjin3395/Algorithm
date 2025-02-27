from itertools import combinations

N, K = map(int, input().split())
home = [list(map(int, input().split())) for _ in range(N)]

# 대피소 조합
combs = list(combinations(range(0, N), K))

dist = []

for shelters in combs:
    mx = 0
    for i in range(N):
        if i in shelters:  # 대피소 설치된 집은 제외
            continue
        x, y = home[i][0], home[i][1]
        mn = 100000
        for s in shelters:
            mn = min(abs(home[s][0]-x) + abs(home[s][1]-y), mn)
            # print("mn:", mn)
        mx = max(mx, mn)
        # print("mx:", mx)
    dist.append(mx)

print(min(dist))
