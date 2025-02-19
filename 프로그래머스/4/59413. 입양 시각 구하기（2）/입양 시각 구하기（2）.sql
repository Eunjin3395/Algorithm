-- 코드를 입력하세요
with recursive hours_cte as (
    select 0 as hour
    union all
    select hour+1 from hours_cte where hour < 23
    
)

SELECT h.hour as HOUR, count(a.animal_id) as 'COUNT'
from hours_cte h
left join ANIMAL_OUTS a
on h.hour = hour(a.datetime)
group by h.hour