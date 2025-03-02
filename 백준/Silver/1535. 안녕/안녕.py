N = int(input())
minus = list(map(int, input().split()))
plus = list(map(int, input().split()))

dp = [0] * 101  # 체력이 100 이하로 유지되도록 설정

for i in range(N):
    for j in range(100, minus[i] - 1, -1):  # 뒤에서부터 갱신 (중복 방지)
        dp[j] = max(dp[j], dp[j - minus[i]] + plus[i])

print(dp[99])  # 최대 기쁨 출력
