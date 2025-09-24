select count(fish_name) as FISH_COUNT, FISH_NAME
from FISH_INFO i 
join FISH_NAME_INFO n
on i.fish_type = n.fish_type
group by fish_name
order by 1 desc
