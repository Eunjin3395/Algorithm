select ANIMAL_TYPE, count(*) as count
from animal_ins
group by ANIMAL_TYPE
order by 1