N = int(input())
arr = list(map(int, input().split()))

result = [0]*N

stack = []
stack.append(N-1)
for i in range(N-2, -1, -1):
    while stack:
        # print("i:", i, ", stack:", stack)
        if arr[stack[-1]] <= arr[i]:
            result[stack[-1]] = i+1
            stack.pop()
        else:
            break
    stack.append(i)

print(*result)
