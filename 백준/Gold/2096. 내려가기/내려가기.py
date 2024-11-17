import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())

scores = list(map(int, input().split()))
mindp = scores
maxdp = scores

for _ in range(N-1):
    scores = list(map(int, input().split()))

    mindp = [min(mindp[0], mindp[1])+scores[0], min(mindp) +
             scores[1], min(mindp[1], mindp[2])+scores[2]]

    maxdp = [max(maxdp[0], maxdp[1])+scores[0], max(maxdp) +
             scores[1], max(maxdp[1], maxdp[2])+scores[2]]
    # print("mindp:", mindp)
    # print("maxdp:", maxdp)

print(max(maxdp), min(mindp))
