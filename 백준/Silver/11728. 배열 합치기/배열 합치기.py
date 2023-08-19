import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

result=[]

a = list(map(int,sys.stdin.readline().split()))
b= list(map(int,sys.stdin.readline().split()))

result+=a
result+=b
result.sort()

for elem in result:
    print(elem,end=" ")