def Z(N, r, c):
    ans = 0

    while N:
        N -= 1

        if r < 2**N and c < 2**N:
            ans = ans

        elif r < 2**N and c >= 2**N:
            ans += 2**(2*N)
            c -= 2**N

        elif r >= 2**N and c < 2**N:
            ans += 2*(2**(2*N))
            r -= 2**N

        elif r >= 2**N and c >= 2**N:
            ans += 3*(2**(2*N))
            r -= 2**N
            c -= 2**N

    return ans

N,r,c = map(int, input().split())
print(Z(N,r,c))