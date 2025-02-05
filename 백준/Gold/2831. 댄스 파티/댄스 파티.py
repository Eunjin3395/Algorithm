N = int(input())
male = list(map(int, input().split()))
female = list(map(int, input().split()))
big_male = []
small_male = []
big_female = []
small_female = []

for p in male:
    if p > 0:
        big_male.append(p)
    else:
        small_male.append(-p)
for p in female:
    if p > 0:
        big_female.append(p)
    else:
        small_female.append(-p)

big_male.sort()
small_male.sort()
big_female.sort()
small_female.sort()

visited_bm = [False]*len(big_male)
visited_sm = [False]*len(small_male)
visited_bf = [False]*len(big_female)
visited_sf = [False]*len(small_female)

# print("big_male:", big_male)
# print("small_male:", small_male)
# print("big_female:", big_female)
# print("small_female:", small_female)

answer = 0

for man in big_male:
    # print("======big man:", man, "=========")
    if len(small_female) == 0:
        break
    left = 0
    right = len(small_female)-1
    female_idx = -1

    while left <= right:
        mid = (left+right)//2
        # print("left:", left, "right:", right, "mid:", mid)

        if man < small_female[mid]:
            female_idx = mid
            right = mid-1
        else:
            left = mid+1
        # print("female_idx:", female_idx)

    if female_idx != -1:
        small_female.pop(female_idx)
        answer += 1

# print("---------------------")
# print(small_female)
# print(answer)
# print("---------------------")

for man in small_male:
    # print("======small man:", man, "=========")
    if len(big_female) == 0:
        break
    left = 0
    right = len(big_female)-1
    female_idx = -1

    while left <= right:
        mid = (left+right)//2
        # print("left:", left, "right:", right, "mid:", mid)

        if man > big_female[mid]:
            female_idx = mid
            left = mid+1

        else:
            right = mid-1
        # print("female_idx:", female_idx)

    if female_idx != -1:
        big_female.pop(female_idx)
        answer += 1
# print("---------------------")
# print(big_female)
# print(answer)
# print("---------------------")

print(answer)
