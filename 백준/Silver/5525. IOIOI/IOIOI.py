N = int(input())
M = int(input())
string = input()

search = "IO"*N+"I"

curr_string = string
cnt = 0
while(True):
    idx = curr_string.find(search)
    if idx == -1:  # 현재 문자열에 IOI가 없는 경우
        break

    cnt += 1
    curr_string = curr_string[idx+1:]

print(cnt)
