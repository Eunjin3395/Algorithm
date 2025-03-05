import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = list(input().strip() for _ in range(N))
queries = list(input().strip() for _ in range(M))

# 집합(set) 사용
prefix_set = set()
for word in S:
    for i in range(1, len(word) + 1):
        prefix_set.add(word[:i])  # 모든 접두사를 집합에 추가

# 접두사 확인
count = sum(1 for query in queries if query in prefix_set)
print(count)
