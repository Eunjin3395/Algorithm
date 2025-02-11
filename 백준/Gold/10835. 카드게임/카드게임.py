from collections import deque
N = int(input())
left = list(map(int, input().split()))
right = list(map(int, input().split()))

# dp[a][b]: 왼쪽 더미에서 a개, 오른쪽 더미에서 b개를 버렸을 때의 최대 점수
dp = [[0]*(N+1) for _ in range(N+1)]

# dp = 오른쪽 1개 버림, 왼쪽 1개 버림, 왼+오른쪽 1개씩 버림 -> 오른쪽 < 왼쪽인 경우
# dp[a][b] = max(dp[a][b-1]+right, dp[a-1][b], dp[a-1][b-1])
# dp = 왼쪽 1개 버림, 왼+오른쪽 1개씩 버림 -> 오른쪽 >= 왼쪽인 경우

for l in range(N-1, -1, -1):
    for r in range(N-1, -1, -1):
        # print("l:", l, ", r:", r, ", :", left[l], right[r])
        if left[l] > right[r]:
            dp[l][r] = max(dp[l][r+1]+right[r], dp[l+1][r], dp[l+1][r+1])
            # print("left > right, dp[", l, "][", r, "]:", dp[l][r])
        else:
            dp[l][r] = max(dp[l+1][r], dp[l+1][r+1])
            # print("left <= right, dp[", l, "][", r, "]:", dp[l][r])


# for row in dp:
#     for col in row:
#         print(col, end=" ")
#     print()

print(dp[0][0])
