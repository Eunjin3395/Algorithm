# 입력 받기
N, r, c = map(int, input().split())


seq = 0


while(N):
    N -= 1
    if r >= 2**N and c >= 2**N:
        # 오른쪽 아래 구간
        seq += 3*(2**(2*N))
        r -= 2**N
        c -= 2**N
    elif r >= 2**N and c < 2**N:
        # 왼쪽 아래 구간
        seq += 2*(2**(2*N))
        r -= 2**N
    elif r < 2**N and c >= 2**N:
        # 오른쪽 위 구간
        seq += 2**(2*N)
        c -= 2**N

print(seq)
