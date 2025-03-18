N = int(input())

arr = list(input() for _ in range(N))
L = len(arr[0])

# 완전탐색??
# 뒤에서부터 1개씩 늘려가면서 key value로 저장해서
# dict의 모든 value가 1이면 그게 답

for i in range(L - 1, -1, -1):
    _dict = {}
    for num in arr:
        if num[i:] in _dict:
            _dict[num[i:]] += 1
            break
        else:
            _dict[num[i:]] = 1

    valid = True
    for v in _dict.values():
        if v > 1:
            valid = False
            break

    if valid:
        print(L - i)
        break

