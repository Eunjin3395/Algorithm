import sys
import heapq
input = sys.stdin.readline

def solve(slime):
    answer = 1
    heapq.heapify(slime)  # 우선순위큐로 변환

    while len(slime) > 1:
        a = heapq.heappop(slime)
        b = heapq.heappop(slime)
        answer *= a * b
        heapq.heappush(slime, a * b)

    return answer

T = int(input())
MOD = 1000000007

for _ in range(T):
    N = int(input())
    slime = list(map(int, input().split()))
    slime.sort()
    print(solve(slime) % MOD)