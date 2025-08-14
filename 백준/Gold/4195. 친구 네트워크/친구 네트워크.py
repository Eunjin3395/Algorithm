from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input())

# 각 집합별 인원수 dict
# 친구 관계 추가할 때마다 각 노드 union 후 루트 노드(집합 번호) 찾기

def find(x):
    if parent_dict[x] != x:
        parent_dict[x] = find(parent_dict[x])
    return parent_dict[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent_dict[a] = b
        cnt_dict[b] += cnt_dict[a]

for _ in range(T):
    F = int(input())
    parent_dict = {}
    cnt_dict = {}
    for _ in range(F):
        a, b = input().split()
        if a not in parent_dict:
            parent_dict[a] = a
            cnt_dict[a] = 1
        if b not in parent_dict:
            parent_dict[b] = b
            cnt_dict[b] = 1

        union(a, b)
        print(cnt_dict[find(b)])
        # print(parent_dict)
        # print(cnt_dict)
