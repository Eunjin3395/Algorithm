-- 코드를 입력하세요
with subquery as(
    SELECT product_id, sum(amount) as total_amount
    from FOOD_ORDER
    where PRODUCE_DATE between date('2022-05-01') and date('2022-05-31')
    group by product_id
)

select f.PRODUCT_ID, f.PRODUCT_NAME, sb.total_amount * f.price as TOTAL_SALES
from FOOD_PRODUCT f
join subquery sb
on f.product_id = sb.product_id
order by 3 desc, 1
