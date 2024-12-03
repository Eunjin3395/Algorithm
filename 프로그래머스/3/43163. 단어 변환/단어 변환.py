def solution(begin, target, words):
    def getAvailable(w):
        result = []
        for x in range(len(words)):
            n = 0
            for i in range(len(w)):
                if w[i] != words[x][i]:
                    n+=1
            if n ==1:
                result.append(x)
        return result
    
    
    def dfs(word,depth):
        # print("dfs called:",word,",depth:",depth)
        if word == target:
            result.append(depth)
        
        next_nodes = getAvailable(word)
        # print("next_nodes:",next_nodes)
        # print("visited:",visited)
        for next_node in next_nodes:
            if not visited[next_node]:
                # print("next visit:",next_node)
                visited[next_node]=True
                dfs(words[next_node],depth+1)
                visited[next_node] = False
         
            
    result = []
    visited = [False for _ in range(len(words))]
    dfs(begin,0)
        
    if result:
        answer=min(result)
    else:
        answer = 0
        
    return answer