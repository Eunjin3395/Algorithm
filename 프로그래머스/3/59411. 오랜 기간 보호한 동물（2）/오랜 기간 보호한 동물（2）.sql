select i.ANIMAL_ID, i.NAME
from ANIMAL_INS i
join ANIMAL_OUTS o
on i.animal_id = o.animal_id
order by o.datetime - i.datetime desc
limit 2