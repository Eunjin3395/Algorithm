import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    parent[a_root] = b_root  # 더 작은 번호로 이동

G = int(input())  # 게이트 수
P = int(input())  # 비행기 수

parent = [i for i in range(G + 1)]  # 0번은 사용 안 함

answer = 0
for _ in range(P):
    g = int(input())
    dock = find(g)
    if dock == 0:
        break
    union(dock, dock - 1)
    answer += 1

print(answer)