# 입력 받기
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = []
for elem in A:
    result.append(elem)

for elem in B:
    result.append(elem)

result.sort()
for elem in result:
    print(elem, end=" ")
