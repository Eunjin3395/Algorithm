import heapq
from collections import defaultdict

def solution(operations):
    maxq = []
    minq=[]
    _dict = defaultdict(int)
    cnt=0
    for opt in operations:
        cmd, val = opt.split()
        val = int(val)

        if cmd == 'I':
            heapq.heappush(minq,val)
            heapq.heappush(maxq,-val)
            _dict[val]+=1
            cnt+=1
        else:
            if cnt==0:
                continue
            if val ==1:
                while True:
                    x = heapq.heappop(maxq)
                    if _dict[-x]>0:
                        _dict[-x]-=1
                        cnt-=1
                        break
            elif val == -1:
                while True:
                    x = heapq.heappop(minq)
                    if _dict[x]>0:
                        _dict[x]-=1
                        cnt-=1
                        break
    # print(minq)
    # print(maxq)
    # print(_dict)
    arr = []
    
    for key, value in _dict.items():
        if value>0:
            arr.append(key)
            
    if not arr:
        return [0,0]
    else:
        arr.sort()
        return[arr[-1],arr[0]]
            
                        
                        
                
            
                
                
        
    
    answer = []
    return answer