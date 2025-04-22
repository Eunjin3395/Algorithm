N = int(input())

# dp[i][a][l] = i일 차까지 출석했고,
#              a = 지각 횟수 (0 or 1)
#              l = 연속 결석 수 (0~2)

dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 1  # 0일차, 지각 0, 결석 0 → 1가지 (아무것도 안함)

for i in range(1, N + 1):
    for a in range(2):     # 지각 0회 or 1회
        for l in range(3):  # 연속 결석 0, 1, 2

            # 1. 출석(P): 연속 결석 0으로 초기화, 지각 횟수 변화 없음
            dp[i][a][0] += dp[i - 1][a][l]

            # 2. 결석(L): 연속 결석 +1, 지각 횟수 변화 없음
            if l < 2:
                dp[i][a][l + 1] += dp[i - 1][a][l]

            # 3. 지각(A): 지각 횟수 +1, 연속 결석 0
            if a < 1:
                dp[i][a + 1][0] += dp[i - 1][a][l]

# for row in dp:
#     for elem in row:
#         print(elem, end=" ")
#     print()

MOD = 1000000
answer = 0
for a in range(2):
    for l in range(3):
        answer = (answer + dp[N][a][l]) % MOD
print(answer)