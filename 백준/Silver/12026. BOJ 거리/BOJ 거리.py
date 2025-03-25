import sys

N=int(sys.stdin.readline())
road=sys.stdin.readline().strip()
d=[1000001]*len(road)
d[0]=0 #첫번째 값은 0으로 설정 
for i in range(1,len(road)):
    if road[i]=='B': # 글자가 B일때
        for j in range(0,i): # 이전에 나온 J의 값에서 해당 B(road[i])를 선택하는 경우의 최솟값으로 dp테이블 업데이트
            if road[j]=='J':
                d[i]=min(d[i],(i-j)*(i-j)+d[j])
    elif road[i]=='O': # 글자가 O일때
        for j in range(0, i):  # 이전에 나온 B의 값에서 해당 O(road[i])를 선택하는 경우의 최솟값으로 dp테이블 업데이트
            if road[j] == 'B':
                d[i] = min(d[i], (i-j)*(i-j)+d[j])
    else: # 글자가 J일때 
        for j in range(0, i):# 이전에 나온 O의 값에서 해당 J(road[i])를 선택하는 경우의 최솟값으로 dp테이블 업데이트
            if road[j] == 'O':
                d[i] = min(d[i], (i-j)*(i-j)+d[j])

if d[N-1]==1000001:# 끝까지 올수 없을 경우
    print(-1) # -1출력
else:
    print(d[N-1])