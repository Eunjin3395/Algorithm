choice = []
arr = []


def comb(index, level):
    # base case
    if(level == 6):
        for elem in choice:
            print(elem, end=" ")
        print()

    for i in range(index, len(arr)):
        choice.append(arr[i])
        comb(i+1, level+1)
        choice.pop()


while True:
    line = list(map(int, input().split()))

    k, arr = line[0], line[1:]

    if k == 0:
        break

    comb(0, 0)
    print()
