n = int(input())
dict = {}

# 딕셔너리에 카드 번호별 장 수 저장
for i in range(n):
    x = int(input())
    if x in dict:
        dict[x]+=1
    else:
        dict[x]=1

# 딕셔너리를 value 기준으로 내림차순 정렬
result = sorted(dict.items(),key = lambda x:(-x[1],x[0]))

print(result[0][0])

