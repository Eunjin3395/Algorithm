# 입력 받기
N = input()

arr = []

for c in N:
    arr.append(int(c))

sorted_arr = sorted(arr, reverse=True)
for elem in sorted_arr:
    print(elem, end="")