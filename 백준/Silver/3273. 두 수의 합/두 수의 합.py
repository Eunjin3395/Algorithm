n = int(input())
arr = list(map(int, input().split()))
x = int(input())

visited = set()
count = 0

for num in arr:
    if x - num in visited:
        count += 1
    visited.add(num)

print(count)