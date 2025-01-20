N = int(input())

A = list(map(int, input().split()))
nge = [-1]*N
stack = []

for i in range(N):
    while stack and A[i] > A[stack[-1]]:
        nge[stack[-1]] = A[i]

        stack.pop()
    stack.append(i)

print(*nge)