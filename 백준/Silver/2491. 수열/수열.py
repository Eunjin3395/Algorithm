N = int(input())
nums = list(map(int, input().split()))

# 그리디
# 이전 인덱스보다 크면 i_cnt +1하고 d_cnt=1
# 이전 인덱스보다 작으면 d_cnt +1하고 c_cnt=1

if N == 1:
    print(1)
    exit()

i_cnt = 1
d_cnt = 1

i_mx = 0
d_mx = 0

for i in range(1, N):
    # print("i:", i, ", num:", nums[i], ", i_cnt:", i_cnt, ", d_cnt:", d_cnt, ", i_mx:", i_mx, ", d_mx:", d_mx)
    if nums[i] == nums[i - 1]:
        i_cnt += 1
        d_cnt += 1
    elif nums[i] > nums[i - 1]:  # 증가
        i_cnt += 1
        d_cnt = 1
    else:  # 감소
        d_cnt += 1
        i_cnt = 1
    d_mx = max(d_mx, d_cnt)
    i_mx = max(i_mx, i_cnt)
    # print("i:", i, ", num:", nums[i], ", i_cnt:", i_cnt, ", d_cnt:", d_cnt, ", i_mx:", i_mx, ", d_mx:", d_mx)

print(max(i_mx, d_mx))
