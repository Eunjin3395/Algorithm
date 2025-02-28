import sys

sys.setrecursionlimit(10**6)

N, K = map(int, sys.stdin.readline().split())

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

answer = (factorial(N) // (factorial(N-K) * factorial(K))) % 10007
print(answer)