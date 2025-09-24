select INGREDIENT_TYPE, sum(h.total_order) as TOTAL_ORDER
from FIRST_HALF h
join ICECREAM_INFO i
on h.flavor = i.flavor
group by i.INGREDIENT_TYPE
order by 2