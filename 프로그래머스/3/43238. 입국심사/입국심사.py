def solution(n, times):
    left = 0 # 최소 시간
    right = max(times)* n # 최대 시간
    
    while left<= right:
        mid = (left+right)//2
        
        people = 0
        
        for time in times:
            people += mid//time
        
        if people >= n: # mid가 찾고자하는 값보다 큼
            answer = mid
            right = mid -1
        else: # mid가 찾고자하는 값보다 작음
            left = mid+1
            
    return answer