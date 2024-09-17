N = int(input())

result = 0
cnt = 0
if(N == 1):
    print(1)
else:
    for i in range(N):
        result += i
        if(result > N):
            break
        cnt += 1
    print(cnt-1)
