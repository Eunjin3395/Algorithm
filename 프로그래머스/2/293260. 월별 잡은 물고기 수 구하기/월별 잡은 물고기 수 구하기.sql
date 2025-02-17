-- 코드를 작성해주세요
SELECT COUNT(*) as FISH_COUNT, MONTH(TIME) as MONTH
from fish_info
group by month(time)
having count(*) >0
order by 2