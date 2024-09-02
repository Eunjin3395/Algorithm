def recursion(N, arr):
  # 1의 존재 여부
    blueExists = False
    for row in arr:
        if 1 in row:
            blueExists = True
            break

    # 0의 존재 여부
    whiteExists = False
    for row in arr:
        if 0 in row:
            whiteExists = True
            break

    if(N == 1):
        if(blueExists):
            global blue
            blue += 1
        else:
            global white
            white += 1
        return
    elif(blueExists and not whiteExists):
        blue += 1
        return
    elif(not blueExists and whiteExists):
        white += 1
        return
    else:
        recursion(N//2, [row[0:N//2] for row in arr[0:N//2]])
        recursion(N//2, [row[N//2:N] for row in arr[0:N//2]])
        recursion(N//2, [row[0:N//2] for row in arr[N//2:N]])
        recursion(N//2, [row[N//2:N] for row in arr[N//2:N]])


blue = 0
white = 0

N = int(input())

array = []

for _ in range(N):
    row = list(map(int, input().split()))
    array.append(row)

recursion(N, array)

print(white)
print(blue)
