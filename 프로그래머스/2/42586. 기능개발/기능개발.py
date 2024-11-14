import math

def solution(progresses, speeds):
    answer = []
    if not progresses:
        return answer
    
    arr = []
    for i in range(len(progresses)):
        days = math.ceil((100-progresses[i])/speeds[i])
        arr.append(days)
    print(arr)
    
    x = 0
    while arr:
        day = arr.pop(0)
        if x<day:
            x = day
            answer.append(0)
        answer[-1]+=1
    
    return answer