# 입력 받기
N = int(input())

# dp[y][x]: 길이가 y인 수의 마지막 자리가 x일 때 오르막의 개수
dp = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N+1)]
dp[1] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# x 1 -> 2
# x 2 -> 3
# x 3 -> 4
# ...
# x 9 -> 10


for i in range(2, N+1):
    for x in range(1, 10):
        dp[i][x] = sum(dp[i-1][:x+1])


print(sum(dp[N]) % 10007)
