# outs를 기준으로 left join
select o.ANIMAL_ID, o.NAME
from ANIMAL_OUTS o
left join ANIMAL_INS i
on o.animal_id = i.animal_id
where i.animal_id is null
order by 1,2