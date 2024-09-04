# 입력 받기
from itertools import combinations

L, C = map(int, input().split())
arr = input().split()

# 모든 가능한 조합 다 뽑고 거기서 최소 1개의 모음, 2개의 자음이 없는 애들은 거르기
all_list = list(combinations(sorted(arr), L))
result = []
for elem in all_list:
    # 모음 개수와 자음 개수 세기
    vowel_count = 0
    consonant_count = 0
    for char in elem:
        if char in "aeiou":
            vowel_count += 1
        else:
            consonant_count += 1

    # 모음이 최소 1개, 자음이 최소 2개인 경우만 처리
    if vowel_count >= 1 and consonant_count >= 2:
        # 조합을 문자열로 변환하여 결과 리스트에 추가
        print(''.join(elem))
