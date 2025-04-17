import sys
input = sys.stdin.readline

N = int(input())
stack = []
count = 0

for _ in range(N):
    x, y = map(int, input().split())

    while stack and stack[-1] > y:
        stack.pop()
        count += 1

    if not stack or stack[-1] < y:
        if y != 0:
            stack.append(y)

# 남아있는 높이 처리
count += len(stack)
print(count)