# 카테고리별 max price 뽑기
# 해당 가격을 갖는 product_name 찾기

with MAX_PRICE_TBL as (
    select category, max(price) as max_price
    from FOOD_PRODUCT
    where category in ('과자','국','김치','식용유')
    group by category
)

select f.CATEGORY, t.MAX_PRICE, f.PRODUCT_NAME
from FOOD_PRODUCT f
join MAX_PRICE_TBL t
on f.category = t.category
where f.price = t.max_price
order by 2 desc