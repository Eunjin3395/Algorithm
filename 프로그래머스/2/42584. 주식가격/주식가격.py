def solution(prices):
    N = len(prices)
    answer = [i for i in range(N-1,-1,-1)]
    
    stack = [0]
    
    for i in range(1,N):
        while stack and prices[stack[-1]] > prices[i]:
            x = stack.pop()
            answer[x] = i-x
        stack.append(i)
    
    return answer