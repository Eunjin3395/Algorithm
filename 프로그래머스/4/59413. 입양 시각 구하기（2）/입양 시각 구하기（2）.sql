with recursive hour_tbl as(
    select 0 as hour
    
    union all
    
    select hour+1 from hour_tbl where hour<23
)

select h.HOUR, count(o.animal_id) as COUNT
from hour_tbl h
left join ANIMAL_OUTS o
on h.hour = hour(o.datetime)
group by h.hour
order by 1