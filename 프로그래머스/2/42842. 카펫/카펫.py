def get_divisor(n):
    result = []
    for i in range(1,n+1):
        if n%1 ==0:
            result.append(i)
    return result

def solution(brown, yellow):
    divisor = get_divisor(yellow)
    
    for x in divisor:
        y = yellow//x
        if (x+2)*(y+2) == brown+yellow and 2*(x+y+2) == brown:
            print(x+2,"*",y+2,"=",brown+yellow)
            if x>=y:
                answer = [x+2,y+2]
            else:
                answer =[y+2,x+2]
    return answer

