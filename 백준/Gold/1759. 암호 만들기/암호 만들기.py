from itertools import combinations

# 입력 받기
L, C = map(int, input().split())
arr = list(input().split())

# 최소 한개의 모음, 두개의 자음이라는 조건

# 암호 후보가 될 문자를 모두 뽑은 후, 정렬해서 출력하기

# 모음, 자음 각각 추출
vowels = ['a', 'e', 'i', 'o', 'u']

mo = []
ja = []
for c in arr:
    if c in vowels:
        mo.append(c)
    else:
        ja.append(c)


# 자음 후보 리스트 생성
ja_comb = list(combinations(ja, 2))

# 최종 암호 문자열 리스트
result = []

for m in range(len(mo)):
    for j in range(len(ja_comb)):
        picked = []

        # 모음 리스트에서 일단 1개 뽑기
        picked.append(mo[m])

        # 자음 후보 리스트에서 일단 2개 뽑기
        picked.append(ja_comb[j][0])
        picked.append(ja_comb[j][1])
        # print(picked)

        # 나머지 모음+자음에서 남은 개수만큼 뽑기
        # 나머지 문자 후보 리스트 생성
        other = arr[:]
        other.remove(mo[m])
        other.remove(ja_comb[j][0])
        other.remove(ja_comb[j][1])

        other_comb = list(combinations(other, L-3))
        for elem in other_comb:
            # 최종 문자 선택 리스트 생성
            final_picked = picked+list(elem)
            final_picked.sort()
            total = ''.join(final_picked)
            if total not in result:
                result.append(total)


result.sort()
for elem in result:
    print(elem)
