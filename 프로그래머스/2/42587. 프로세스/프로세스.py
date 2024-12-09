def solution(priorities, location):
    execute = []
    arr = list(enumerate(priorities))
    # print(arr)
    while arr:
        priority = arr.pop(0)
        
        isLargest = True
        for i in range(len(arr)):
            if arr[i][1] > priority[1]:
                isLargest = False
                break
        
        if(isLargest):
            execute.append(priority)
        else:
            arr.append(priority)
        
    
    for i in range(len(execute)):
        if execute[i][0] == location:
            return i+1