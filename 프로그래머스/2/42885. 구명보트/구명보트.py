def solution(people, limit):
    people.sort()
    
    answer = 0
    start = 0
    end = len(people)-1
    
    while start<=end:
        if people[start]+people[end]<=limit: # 두명 같이 구출 가능
            start+=1
            end-=1
        else: # 큰 사람 한명만 구출 가능
            end-=1
        answer+=1
            
            
    return answer
