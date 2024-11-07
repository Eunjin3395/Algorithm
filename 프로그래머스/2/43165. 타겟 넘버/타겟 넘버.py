def solution(numbers, target):
    value = [0]
    for num in numbers:
        temp=[]
        for elem in value:
            temp.append(elem+num)
            temp.append(elem-num)
        value=temp
    
    #print("value:",value)
    answer = 0
    for n in value:
        if n == target:
            answer+=1
    return answer