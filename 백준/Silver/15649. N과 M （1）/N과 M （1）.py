from itertools import permutations

N, M = map(int, input().split())

for comb in permutations(range(1, N + 1), M):
    print(' '.join(map(str, comb)))
