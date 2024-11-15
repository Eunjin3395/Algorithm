def solution(N, number):
    answer = -1
    if number == N:
        return 1
    
    _li = [set() for i in range(8)]
    for i in range(len(_li)):
        _li[i].add(int(str(N)*(i+1)))
        
    for i in range(1,8):
        for j in range(i):
            for op1 in _li[j]:
                for op2 in _li[i-j-1]:
                    _li[i].add(op1+op2)
                    _li[i].add(op1-op2)
                    _li[i].add(op1*op2)
                    if op2 != 0:
                        _li[i].add(op1//op2)
        if number in _li[i]:
            answer = i+1
            break
    
    return answer