select i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
from ANIMAL_INS i
join ANIMAL_OUTS o
on i.animal_id = o.animal_id
where i.sex_upon_intake like '%Intact%'
and (o.sex_upon_outcome like '%Spayed%' or o.sex_upon_outcome like '%Neutered%')
order by 1