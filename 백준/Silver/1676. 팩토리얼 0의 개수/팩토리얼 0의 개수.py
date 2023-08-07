import sys

def factorial(n):
    if(n<=1):
        return 1
    return factorial(n-1)*n

N=int(sys.stdin.readline())
fact = factorial(N)
fact_list = list(map(int,str(fact)))
count=0
for i in reversed(range(len(fact_list))):
    if(fact_list[i]==0):
        count+=1
    else:
        break

print(count)
