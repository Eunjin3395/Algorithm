from itertools import product

def solution(word):
    alphabet = ["A","E","I","O","U"]
    
    # 모음사전 list 생성
    total = []
    for i in range(1,6):
        for elem in list(product(alphabet,repeat=i)):
            total.append(''.join(elem))
    
    total.sort()
        
    answer = total.index(word)+1
    return answer