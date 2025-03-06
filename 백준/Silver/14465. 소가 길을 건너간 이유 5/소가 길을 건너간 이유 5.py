N, K, B = map(int, input().split())

err = list(int(input()) for _ in range(B))

light = [1] * N

for x in err:
    light[x - 1] = 0

# print(light)

# 0 ~ K까지의 수리할 신호등 개수
cnt = K - sum(light[:K])
arr = []
arr.append(cnt)

for i in range(1, N - K + 1):
    if light[i - 1] == 0:
        cnt -= 1
    if light[i + K - 1] == 0:
        cnt += 1
    arr.append(cnt)

print(min(arr))
