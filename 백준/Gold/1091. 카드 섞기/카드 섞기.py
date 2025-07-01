# i번째 위치에 있던 카드는 S[i]번째 위치로 이동
# 목표로 하는 카드 분배: 0 1 2 0 1 2 0 1 2 ...
# 처음의 카드 분배: P[i]


# 연산 과정 중에 기존에 나왔던 애가 또 나오면 그때부턴 같은 결과의 반복.. 원하는 결과 만들 수 없다

# P: 시작 카드 배열
# P -> 0 1 2 ... 로 만들어가는 과정

N = int(input())

P = list(map(int, input().split()))
S = list(map(int, input().split()))

def shuffle(curr_arr):
    new_arr = [0] * N

    for i in range(N):
        new_arr[S[i]] = curr_arr[i]

    return new_arr

def same(curr, target):
    for i in range(N):
        if curr[i] != target[i]:
            return False
    return True


target = []  # 만들어야할 첫 카드 배열
for i in range(N):
    target.append(i % 3)


if same(P, target):  # 역연산 아예 필요 없는 경우
    print(0)
    exit()

arr_set = set()
curr_arr = P
t = 0

while True:
    t += 1
    new_arr = shuffle(curr_arr)
    tp = tuple(new_arr)

    if tp in arr_set:
        print(-1)
        break

    arr_set.add(tp)

    if same(new_arr, target):
        print(t)
        break
    curr_arr = new_arr
