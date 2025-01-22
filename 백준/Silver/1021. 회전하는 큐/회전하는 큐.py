from collections import deque

N, M = map(int, input().split())

arr = [i+1 for i in range(N)]
target = list(map(int, input().split()))

# 뽑고자 하는 원소의 idx가 l//2보다 큰 경우: 3번 연산
# l//2보다 작은 경우: 2번 연산


cnt = 0
for i in range(M):
    if(arr[0] == target[i]):
        arr.pop(0)
    else:
        while(arr[0] != target[i]):
            idx = arr.index(target[i])
            if idx >= len(arr)/2:
                arr.insert(0, arr.pop())
            else:
                arr.append(arr.pop(0))
            cnt += 1
        arr.pop(0)

print(cnt)
