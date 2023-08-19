import sys

global countM
global count0
global count1




def divide(n, sX,sY,eX,eY):
    
    global countM
    global count0
    global count1

    isM,is0,is1=0,0,0

    for r in range(sX,eX):
        if(-1 in matrix[r][sY:eY]):
            isM=1
        if( 0 in matrix[r][sY:eY]):
            is0=1
        if(1 in matrix[r][sY:eY]):
            is1=1
    
    if(isM and not is0 and not is1):
        countM+=1
        return 0
    if(not isM and is0 and not is1):
        count0+=1
        return 0
    if(not isM and not is0 and is1):
        count1+=1
        return 0

    if(sX+1==eX and sY+1==eY): # 요소가 하나만 남았을 경우
        if(matrix[sX][sY]==-1):
            countM+=1
        elif(matrix[sX][sY]==0):
            count0+=1
        else:
            count1+=1
        return 0
    


    M=int(n/3)

    divide(M,sX,sY,sX+M,sY+M)
    divide(M,sX,sY+M,sX+M,sY+2*M)
    divide(M,sX,sY+2*M,sX+M,sY+3*M)

    divide(M,sX+M,sY,sX+2*M,sY+M)
    divide(M,sX+M,sY+M,sX+2*M,sY+2*M)
    divide(M,sX+M,sY+2*M,sX+2*M,sY+3*M)

    divide(M,sX+2*M,sY,sX+3*M,sY+M)
    divide(M,sX+2*M,sY+M,sX+3*M,sY+2*M)
    divide(M,sX+2*M,sY+2*M,sX+3*M,sY+3*M)


N = int(sys.stdin.readline())

matrix = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]

countM=0
count0=0
count1=0

divide(N,0,0,N,N)

print(countM)
print(count0)
print(count1)
        