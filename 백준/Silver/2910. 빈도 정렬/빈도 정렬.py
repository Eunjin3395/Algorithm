N, C = map(int, input().split())
input_arr = list(map(int, input().split()))

_dict = {}  # 1: [2,1] # [빈도, 등장 인덱스]

for i in range(len(input_arr)):
    if input_arr[i] in _dict:
        _dict[input_arr[i]][0] += 1
    else:
        _dict[input_arr[i]] = [1, i]

# sorted_dict = sorted(_dict.keys(), key=lambda x: (_dict[x][0], _dict[x][1]), reverse=False)

sorted_dict = sorted(_dict.items(), key=lambda x: (-x[1][0], x[1][1]))

# print(sorted_dict)

for i in range(len(sorted_dict)):
    print((str(sorted_dict[i][0]) + " ") * sorted_dict[i][1][0], end="")
