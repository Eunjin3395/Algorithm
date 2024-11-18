import sys
input = sys.stdin.readline

# 입력 받기
T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    for _ in range(N):
        a, b = map(int, input().split())
        arr.append([a, b])

    # 서류 점수를 기준으로 먼저 정렬
    arr = sorted(arr, key=lambda x: x[0])

    cnt = 1
    num = arr[0][1]
    for i in range(1, N):
        if arr[i][1] < num:
            num = arr[i][1]  # 합격 기준 면접 순위 업데이트
            cnt += 1

    print(cnt)
