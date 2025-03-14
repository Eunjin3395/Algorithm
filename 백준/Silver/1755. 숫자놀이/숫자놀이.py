M, N = map(int, input().split())

mapping = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}
_dict = {}

for n in range(M, N + 1):
    arr = list(str(n))
    string = ""
    for char in arr:
        string = ' '.join([string, mapping[char]])
    _dict[string[1:]] = n

result = []
for key in sorted(_dict.keys()):
    result.append(_dict[key])

for i in range(len(result)):
    print(result[i], end=" ")
    if i % 10 == 9:
        print()
