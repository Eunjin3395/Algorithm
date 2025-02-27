N = int(input())

if N == 1:
    print(1)
    exit()
elif N == 2:
    print(2)
    exit()

now = 0
before1 = 2
before2 = 1

for i in range(2, N):
    now = (before1+before2) % 15746
    before2 = before1
    before1 = now

# print(dp)
print(now)
