import sys

s, e, q = map(str, sys.stdin.readline().split())
dic = {}
answer = {}

# 반복문을 통해 시간과 닉네임을 입력받는다.
for i in sys.stdin:
    time, nick = i.rstrip().split()

    # 개총 시작시간(포함)보다 일찍 들어온 사람을 dic 입력
    if time <= s:
        dic[nick] = time

    # 개총 종료시간과 스트리밍 종료시간 사이에 들어온 사람을 확인
    elif e <= time <= q:
        # 개총 시작시간에보다 일찍 들어온 사람이라면 answer 입력
        if nick in dic:
            answer[nick] = 1

print(len(answer))