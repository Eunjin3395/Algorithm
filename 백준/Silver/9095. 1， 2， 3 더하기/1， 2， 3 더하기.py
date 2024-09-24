# 입력 받기
T = int(input())
arr = []
for _ in range(T):
    arr.append(int(input()))

# dp[x]: x를 1,2,3의 합으로 나타내는 방법의 수

dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

for i in range(T):
    print(dp[arr[i]])
