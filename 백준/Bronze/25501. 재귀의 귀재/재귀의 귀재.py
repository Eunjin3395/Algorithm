def recursive(s, startIdx, endIdx):
    global cnt
    cnt += 1
    if startIdx >= endIdx:
        return 1
    elif s[startIdx] != s[endIdx]:
        return 0

    return recursive(s, startIdx + 1, endIdx - 1)


def isPalindrom(s):
    return recursive(s, 0, len(s) - 1)


n = int(input())

s = [input() for _ in range(n)]

for elem in s:
    cnt = 0
    print(isPalindrom(elem), cnt)
