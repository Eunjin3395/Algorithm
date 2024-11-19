from collections import deque

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    
    dy = [1,0,-1,0]
    dx= [0,-1,0,1]
    
    visited = [[False]*M for _ in range(N) ]
    
    q = deque()
    q.append((0,0,1)) # y,x,dist
    visited[0][0] = True
    
    while q:
        y,x,d = q.popleft()
        
        if y == N -1 and x == M-1: # 상대 진영에 도착
            return d
        
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            
            if 0<= ny<N and 0<=nx<M and not visited[ny][nx]:
                if maps[ny][nx]: # 다음 노드가 벽이 아닐 때에만
                    q.append((ny,nx,d+1))
                    visited[ny][nx] = True
                    
    return -1