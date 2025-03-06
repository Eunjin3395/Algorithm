import sys
input = sys.stdin.readline

string = input().strip()
Q = int(input())

# 문자열의 0 ~ x번째 인덱스 까지에서 각 알파벳의 등장 개수 세기
# l, r 입력에 대해 r까지의 개수 - l-1까지의 개수

alphabet = [[0] * len(string) for _ in range(26)]

for i in range(len(string)):
    alphabet[ord(string[i]) - 97][i] += 1

# for row in alphabet:
#     print(row)

for _ in range(Q):
    char, l, r = input().split()
    l, r = int(l), int(r)
    n = ord(char) - 97
    if l == 0:
        print(sum(alphabet[n][:r + 1]))
    else:
        print(sum(alphabet[n][:r + 1]) - sum(alphabet[n][:l]))
        # print("aa", alphabet[n][r], alphabet[n][l - 1])

