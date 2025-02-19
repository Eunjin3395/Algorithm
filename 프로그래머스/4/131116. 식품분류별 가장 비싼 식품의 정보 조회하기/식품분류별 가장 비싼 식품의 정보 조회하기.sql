-- 코드를 입력하세요
with max_table as (
    select category, max(price) as max_price
    from food_product
    where category in ('과자', '국','김치','식용유')
    group by category
)


SELECT f.CATEGORY, f.price as MAX_PRICE, f.PRODUCT_NAME
from FOOD_PRODUCT as f
where exists (
    select 1
    from max_table as mx
    where f.price = mx.max_price and f.category = mx.category
)
order by f.price desc