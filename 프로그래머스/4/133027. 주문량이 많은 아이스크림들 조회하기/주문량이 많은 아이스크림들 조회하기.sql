-- 코드를 입력하세요
with cte as (
SELECT flavor, sum(total_order) as total_order
    from JULY
    group by flavor
    
    union all
    
    select flavor, total_order
    from FIRST_HALF
),
order_table as (
    select flavor, sum(total_order) as sum
    from cte
    group by flavor
    order by sum desc
)

select flavor
from order_table
limit 3