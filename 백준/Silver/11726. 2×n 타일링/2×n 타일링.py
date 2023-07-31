x = int(input())

d = [0]*(x+1)

d[1]=1
if(x>1):
  d[2]=2

for i in range(3,x+1):
    d[i]=(d[i-1]+d[i-2])%10007
print(d[x])