N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

# O O X
# O X O
# X O O

dp = [0]*(N)
if N == 1:
    print(arr[0])
    exit()
elif N == 2:
    print(arr[0]+arr[1])
    exit()

dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(dp[1], dp[0]+arr[2], arr[1]+arr[2])


for i in range(3, N):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(dp[N-1])
