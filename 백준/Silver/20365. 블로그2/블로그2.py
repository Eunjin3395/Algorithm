N = int(input())
arr = list(input())

# 그리디
# 파란색으로 모두 칠하고 (cnt+1)
# 빨간색 구간의 개수 구해서 그만큼 cnt에 더하기

# 빨간색으로 모두 칠하고
# 파란색 구간의 개수 구해서 그만큼 cnt에 더하기

rmin = 1
cnt = 0
flag = False
for i in range(N):
    if arr[i] == 'R':
        if not flag:
            flag = True
            cnt += 1
    else:
        flag = False

rmin += cnt

bmin = 1
cnt = 0
flag = False
for i in range(N):
    if arr[i] == 'B':
        if not flag:
            flag = True
            cnt += 1
    else:
        flag = False

bmin += cnt
# print(rmin, bmin)
print(min(rmin, bmin))
