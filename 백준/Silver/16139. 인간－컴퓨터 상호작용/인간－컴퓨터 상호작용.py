import sys
input = sys.stdin.readline

string = input().strip()
Q = int(input())

# dp[x][y]: x번째 인덱스까지 y알파벳의 등장 횟수
dp = [[0] * 26 for _ in range(len(string))]
n = ord(string[0]) - 97
dp[0][n] += 1

# dp[x] = dp[x-1] 복사하고 x번째 문자의 개수만 +1
for i in range(1, len(string)):
    dp[i] = dp[i - 1][:]

    n = ord(string[i]) - 97
    dp[i][n] += 1

for _ in range(Q):
    char, l, r = input().split()
    l, r = int(l), int(r)
    n = ord(char) - 97
    if l == 0:
        print(dp[r][n])
    else:
        print(dp[r][n] - dp[l - 1][n])
