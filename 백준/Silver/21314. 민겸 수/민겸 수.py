S = input()

# 최댓값: M은 최대한 나누고, K는 그때그때 변환
max_ans = ''
m_cnt = 0
for ch in S:
    if ch == 'M':
        m_cnt += 1
    else:  # 'K'
        if m_cnt > 0:
            max_ans += '5' + '0' * m_cnt
            m_cnt = 0
        else:
            max_ans += '5'
for _ in range(m_cnt):  # 남은 M 처리
    max_ans += '1'

# 최솟값: M은 최대한 묶고, K가 오면 M + K 묶음 처리
min_ans = ''
m_cnt = 0
for ch in S:
    if ch == 'M':
        m_cnt += 1
    else:  # 'K'
        if m_cnt > 0:
            min_ans += '1' + '0' * (m_cnt - 1)
            m_cnt = 0
        min_ans += '5'
if m_cnt > 0:
    min_ans += '1' + '0' * (m_cnt - 1)

print(max_ans)
print(min_ans)