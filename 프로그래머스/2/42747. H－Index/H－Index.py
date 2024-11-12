def solution(citations):
    # citations=[0,3,4,7,7,7,7,7,7,7,15]
    citations.sort()
    answer = 0
    for i in range(len(citations)):
        if len(citations)-i <= citations[i]:
            print(len(citations)-(i),"<=",citations[i])
            answer = len(citations)-i
            break
            # print("answer: ",answer)
            
    return answer