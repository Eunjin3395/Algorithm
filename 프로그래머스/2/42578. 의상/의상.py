def solution(clothes):
    dict_table={}
    for elem in clothes:
        if elem[1] in dict_table:
            dict_table[elem[1]]+=1
        else:
            dict_table[elem[1]]=1
    print(dict_table)
    
    answer = 1
    for v in dict_table.values():
        answer *= (v+1)
        
    return answer - 1