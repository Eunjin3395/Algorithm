import sys

def func(queue,k):
    result = []
    num = k-1
    for i in range(len(queue)):
        if(num<len(queue)):
            result.append(queue.pop(num))
            num+=k-1
        elif(num>=len(queue)):
            num=num%len(queue)
            result.append(queue.pop(num))
            num+=k-1
    return result

N,k = map(int,sys.stdin.readline().rstrip().split())
queue=[]
for i in range(1,N+1):
    queue.append(i)


result = func(queue,k)
print("<",end="")
for i in range(N):
    if(i==N-1):
        print(result[i],end="")
    else:
        print(result[i],end=", ")
print(">",end="")
