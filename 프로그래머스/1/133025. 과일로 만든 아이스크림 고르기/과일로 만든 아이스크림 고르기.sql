select h.flavor
from FIRST_HALF h
join ICECREAM_INFO i
on h.flavor = i.flavor
where i.ingredient_type = 'fruit_based'
group by h.flavor
having sum(h.total_order)>3000
order by sum(h.total_order) desc