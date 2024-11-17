from itertools import permutations

def solution(k, dungeons):
    answer = -1
    orders = list(permutations(range(len(dungeons))))
    for order in orders:
        # print("==============")
        # print("order:",order)
        num = 0
        left_score = k
        for i in order:
            req_score = dungeons[i][0]
            spend_score = dungeons[i][1]
            # print(i,": req:",req_score,", spend:",spend_score, ", left:",left_score)
            
            if left_score < req_score:
                break
            
            left_score-=spend_score
            num+=1
        # print("num:",num)
        answer = max(answer,num)
        # print("answer:",answer)
        
    return answer