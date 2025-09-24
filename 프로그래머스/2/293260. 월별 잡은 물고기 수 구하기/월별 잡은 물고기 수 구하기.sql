# 월별 잡은 물고기 수
select count(id) as FISH_COUNT, month(time) as MONTH
from FISH_INFO
group by month(time)
having count(*)>0
order by 2