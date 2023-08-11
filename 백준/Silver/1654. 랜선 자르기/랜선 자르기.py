import sys
K,N=map(int,sys.stdin.readline().rstrip().split())

li = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

start=1
end=max(li)

while(start<=end):
    mid=(start+end)//2
    num=0

    for elem in li:
        num+=elem//mid # 각 랜선 분할 시 나오는 개수
    
    if(num>=N): # 현재 값으로는 분할 가능하다는 의미 -> 더 큰 수에서 탐색해야함
      start= mid+1
    else:
      end=mid-1

print(end)