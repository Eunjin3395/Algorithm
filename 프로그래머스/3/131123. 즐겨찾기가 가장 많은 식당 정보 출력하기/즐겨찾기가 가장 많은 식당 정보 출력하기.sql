-- 코드를 입력하세요
with subquery as (
select food_type, max(favorites) as max_favorites
from rest_info
group by food_type
)

SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from REST_INFO i
where exists (
    select 1
    from subquery s
    where s.food_type = i.food_type and s.max_favorites = i.favorites
)
order by 1 desc