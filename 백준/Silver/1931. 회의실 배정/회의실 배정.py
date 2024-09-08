# 입력 받기
N = int(input())

arr = []


for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])

sorted_arr = sorted(arr, key=lambda x: (x[1], x[0]))

result = 0
endTime = 0

for time in sorted_arr:
    if(time[0] >= endTime):
        result += 1
        endTime = time[1]

print(result)
