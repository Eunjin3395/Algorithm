with MAX_REST as(
    select food_type, max(favorites) as max_favorites
    from rest_info
    group by food_type
)

select i.FOOD_TYPE, i.REST_ID, i.REST_NAME, i.FAVORITES
from REST_INFO i
join MAX_REST m
on i.food_type = m.food_type
where i.favorites = m.max_favorites
order by 1 desc