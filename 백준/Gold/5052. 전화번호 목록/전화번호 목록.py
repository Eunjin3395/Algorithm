import sys
import math
input = sys.stdin.readline

def solve(numbers):
    numbers.sort()
    for i in range(len(numbers) - 1):  # 정렬되어 있으므로 i번째는 i+1번째와만 비교해보면 된다
        if numbers[i] == numbers[i + 1][0:len(numbers[i])]:
            print("NO")
            return False
    print("YES")
    return True

t = int(input())

for _ in range(t):
    numbers = []
    n = int(input())
    for _ in range(n):
        numbers.append(input().strip())
    solve(numbers)