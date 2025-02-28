import sys
input = sys.stdin.readline

# 입력 받기
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# DP 배열 초기화
dp_no_remove = [0] * n
dp_remove = [0] * n

# 초기값 설정
dp_no_remove[0] = arr[0]
dp_remove[0] = arr[0]
max_sum = arr[0]

# DP 진행
for i in range(1, n):
    dp_no_remove[i] = max(dp_no_remove[i-1] + arr[i], arr[i])
    dp_remove[i] = max(dp_remove[i-1] + arr[i], dp_no_remove[i-1])
    max_sum = max(max_sum, dp_no_remove[i], dp_remove[i])

print(max_sum)