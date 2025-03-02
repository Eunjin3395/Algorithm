N = int(input())
color = input()
rcolor = color[::-1]

r_idx = color.find('R')
b_idx = color.find('B')

# 모두 같은 색으로 이루어진 경우
if r_idx == -1 or b_idx == -1:
    print(0)
    exit()

# R을 오른쪽에 두는 경우
# 뒤에서부터 앞으로, B의 마지막 idx ~ 0번째까지에서 R의 개수
b_last_idx = N - rcolor.find('B') - 1
r_cnt = 0
for i in range(b_last_idx, -1, -1):
    if color[i] == 'R':
        r_cnt += 1

# print(r_cnt)

# B를 오른쪽에 두는 경우
# 뒤에서부터 앞으로, R의 마지막 idx ~ 0번째까지에서 B의 개수
r_last_idx = N - rcolor.find('R') - 1
b_cnt = 0
for i in range(r_last_idx, -1, - 1):
    if color[i] == 'B':
        b_cnt += 1

# print(b_cnt)

print(min(r_cnt, b_cnt))
